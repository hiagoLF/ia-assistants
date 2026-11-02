#!/usr/bin/env python3
"""Generate selectable PDFs through WeasyPrint; stage, count, and publish exclusively."""
import argparse
import html
import json
from pathlib import Path
import re
import shutil
import subprocess
from string import Template
import tempfile

ROOT = Path(__file__).resolve().parents[1]

def rich(value):
    if isinstance(value, str):
        return html.escape(value)
    if not isinstance(value, list):
        raise ValueError('Text must be a string or a list of text/bold/italic segments')
    result = []
    for segment in value:
        text = html.escape(segment['text'])
        if segment.get('bold'): text = '<b>' + text + '</b>'
        if segment.get('italic'): text = '<i>' + text + '</i>'
        result.append(text)
    return ''.join(result)

def p(cls, value):
    return f'<p class="{cls}">{rich(value)}</p>'

def contact(data, letter=False):
    email = html.escape(data['email'], quote=True)
    linkedin = html.escape(data['linkedin'], quote=True)
    if not re.fullmatch(r'[A-Za-z0-9./_-]+', data['linkedin']):
        raise ValueError('LinkedIn must be its displayed domain/path, without a scheme')
    phone, location = rich(data['phone']), rich(data['location'])
    if letter:
        def icon(name):
            uri = (ROOT/'assets/icons'/f'{name}.png').as_uri()
            return f'<img src="{uri}" alt="" style="height:10pt;vertical-align:middle">'
        return f'<p class="contact">{icon("email")}<a href="mailto:{email}">{email}</a> {icon("phone")} {phone} {icon("link")}<a href="https://{linkedin}">{linkedin}</a> {icon("location")}{location}</p>'
    return f'<p class="contact"><a href="mailto:{email}">{email}</a> | {phone} | <a href="https://{linkedin}">{linkedin}</a> | {location}</p>'

def content(data, kind):
    out = [f'<h1>{rich(data["name"])}</h1>']
    if kind == 'resume':
        out.extend([p('headline', data['headline']), contact(data), '<h2>Summary</h2>',
                    p('summary', data['summary']), '<h2 class="experience-heading">Experience</h2>'])
        for index, job in enumerate(data['jobs']):
            job_class = 'job divided' if index < len(data['jobs'])-1 else 'job'
            out.append(f'<section class="{job_class}">' + p('job-title', job['title']))
            out.append('<div class="job-meta"><span class="job-location"><b class="job-company">' + rich(job['company']) + '</b> | ' + rich(job['location']) + '</span><span class="job-date">' + rich(job['dates']) + '</span></div>')
            if job.get('description'): out.append(p('description', job['description']))
            for achievement in job['achievements']:
                cls = 'achievement calibri' if job.get('body_font') == 'calibri' else 'achievement'
                out.append(p(cls, '• ' + achievement))
            out.append(p('skills', [{'text':'Skills: ', 'bold':True}, {'text':job['skills']}]))
            out.append('</section>')
        for key, heading in [('education','Education'),('courses','Courses'),('languages','Languages')]:
            out.append('<h2 class="section-heading">' + heading + '</h2><section class="section-list">')
            out.extend(p('entry', item) for item in data[key])
            out.append('</section>')
    else:
        out.extend([contact(data, True), '<h2>Cover Letter</h2>', p('salutation', data['salutation'])])
        out.extend(p('letter-paragraph', item) for item in data['paragraphs'])
        out.extend([p('closing', data['closing']), p('signature', data['name'])])
    return '\n'.join(out)

def page_count(path):
    report = subprocess.run(['pdfinfo', str(path)], check=True, capture_output=True, text=True,
                            env={**__import__('os').environ, 'LC_ALL':'C'}).stdout
    match = re.search(r'^Pages:\s+(\d+)', report, re.M)
    if not match: raise RuntimeError('pdfinfo did not report Pages')
    return int(match.group(1))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--kind', choices=['resume','cover-letter'], required=True)
    parser.add_argument('--data', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--max-pages', type=int)
    args = parser.parse_args()
    output_root = ROOT.parents[2] / 'generated'
    args.output = args.output.resolve()
    if not args.output.is_relative_to(output_root.resolve()):
        parser.error('Output must be inside the project generated directory')
    maximum = args.max_pages if args.max_pages is not None else (4 if args.kind == 'resume' else 1)
    if maximum < 1: parser.error('--max-pages must be positive')
    for command in ['weasyprint', 'pdfinfo']:
        if not shutil.which(command): parser.error(f'Missing {command}; read references/commands.md')
    if args.output.exists(): parser.error('Output exists; choose a new version filename')
    data = json.loads(args.data.read_text(encoding='utf-8'))
    document = content(data, args.kind)
    css = (ROOT/'assets/style.css').read_text(encoding='utf-8')
    # Absolute local font URIs allow temporary HTML to live outside the skill directory.
    css = css.replace("url('fonts/", "url('" + (ROOT/'assets/fonts').as_uri() + '/')
    template = Template((ROOT/f'assets/{args.kind}.html').read_text(encoding='utf-8'))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='fit-resume-') as temporary:
        folder = Path(temporary)
        draft, candidate = folder/'document.html', folder/'document.pdf'
        cache = folder/'cache'
        cache.mkdir()
        env = {**__import__('os').environ, 'XDG_CACHE_HOME':str(cache)}
        # Body 10.5pt -> floor 9.5pt; 11pt -> 9.95pt. Keep name and contacts readable.
        for scale in [1, 0.975, 0.95, 0.925, 9.5/10.5]:
            sized_css = re.sub(r'calc\(([\d.]+)pt \* var\(--scale\)\)',
                               lambda match: f'{float(match[1])*scale:.5f}pt', css)
            draft.write_text(template.substitute(title=html.escape(args.kind+' - '+data['name']),
                css=sized_css, scale=str(scale), content=document), encoding='utf-8')
            subprocess.run(['weasyprint','--encoding','utf-8',str(draft),str(candidate)],check=True,env=env)
            pages = page_count(candidate)
            if pages <= maximum:
                # Exclusive creation prevents a race from overwriting a previous version.
                try:
                    with args.output.open('xb') as target, candidate.open('rb') as source:
                        shutil.copyfileobj(source, target)
                except FileExistsError:
                    raise SystemExit('Output appeared during rendering; choose a new filename')
                print(json.dumps({'output':str(args.output.resolve()), 'pages':pages,
                                  'font_scale':round(scale,5), 'max_pages':maximum}))
                return
        raise SystemExit(f'OVERFLOW: {pages} pages at minimum font size. Shorten the data text, then rerun with a new unused filename. No final PDF was saved.')

if __name__ == '__main__':
    main()
