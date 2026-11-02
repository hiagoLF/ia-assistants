---
name: build-resume-cover-letter-from-template
description: Gerar PDFs de resume e cover letter a partir dos templates HTML de Hiago Leão com WeasyPrint, conferir páginas com pdfinfo, ajustar fontes antes do texto e preservar versões.
---

# Build resume and cover letter from template

Use os templates desta skill para renderizar conteúdos já preparados. A fonte de dados do perfil é `../fit-resume-for-job/references/`: leia as transcrições e as atualizações autorizadas. Use a skill irmã local deste projeto. Templates e fixtures preservam a aparência e o texto original para validação visual; não os use para inferir o perfil atual nem para sobrepor correções.

## Templates e fidelidade

- `assets/resume.html` e `assets/cover-letter.html`: templates de fluxo para conteúdo adaptado, com estilos em `assets/style.css`.
- `assets/source-resume.html` e `assets/source-cover-letter.html`: reproduções HTML de referência dos anexos, com tipografia e coordenadas medidas dos PDFs. Use apenas para comparar o visual original; posições fixas não devem ser usadas para uma candidatura de texto variável.
- `assets/source-resume.json` e `assets/source-cover-letter.json`: fixtures com o conteúdo original, exclusivamente para verificar o renderer. A fixture da carta mantém inclusive a afirmação antiga de engajamento 4×; ela não pode passar para candidaturas novas. A correção autorizada é consumo de materiais 5× maior.
- Leia [references/layout.md](references/layout.md) quando precisar ajustar o visual; leia [references/input-schema.md](references/input-schema.md) antes de preparar a entrada JSON.

Não substitua o layout por outro design. Preserve A4 medido em 596×842pt, coluna única, margens, hierarquia, linhas divisórias, contatos clicáveis, estilos de corpo e listas do original. Conteúdo variável flui naturalmente; as reproduções de referência preservam os originais separadamente. Não achate páginas em imagens.

O limite padrão é **4 páginas para resume e 1 para cover letter**, sem obrigação de preencher o limite. Para resumes adaptados, confira antes da renderização o formato definido na skill irmã `fit-resume-for-job`: descrições de empresas iguais às originais, salvo ajustes pontuais de palavras-chave comprovadas; cada realização em um bullet de 35 a 65 palavras, na ordem **o que foi feito → resultados e métricas → tecnologias**. Preserve os originais e fixtures históricos sem reescrevê-los para atender a essas regras de adaptação.

O campo `headline` pode ser definido independentemente no resume e na cover letter: **Senior Frontend Software Engineer** para foco frontend ou **Senior Software Engineer** para foco fullstack/engenharia de software mais ampla, conforme a skill de adaptação. A mesma adaptação se aplica aos cargos históricos em `jobs[].title` e às menções a cargos na carta, conforme autorizado pelo usuário. Na carta, `headline` é opcional e aparece abaixo do nome quando informado; o título de seção “Cover Letter” permanece. Mantenha as transcrições e fixtures originais intactas.

## Procedimento

1. Verifique `weasyprint` e `pdfinfo`. Se faltar algum, instale conforme [references/commands.md](references/commands.md), respeitando as permissões do ambiente. Os comandos CLI foram pesquisados e testados em subagente antes da criação desta skill; não precisa repetir a delegação a cada execução.
2. Prepare JSON de entrada numa pasta temporária, com fatos das referências e da conversa cujo uso tenha sido autorizado. Obtenha caminhos inéditos com `../fit-resume-for-job/scripts/new_run.py --company EMPRESA --job VAGA --kind resume` (ou `--kind cover-letter`). Os caminhos ficam em `generated/<empresa-slug>/<vaga-slug>/` na raiz de `jobs-applications`, nunca dentro de uma skill. Na invocação independente, também use nomes inéditos; nunca substitua um PDF existente.
3. Execute o helper por documento, substituindo os caminhos absolutos conforme a instalação:

```bash
python3 /caminho/build-resume-cover-letter-from-template/scripts/render.py \
  --kind resume --data /temporario/resume.json \
  --output /caminho/jobs-applications/generated/empresa/vaga/resume-IDENTIFICADOR.pdf --max-pages 4
python3 /caminho/build-resume-cover-letter-from-template/scripts/render.py \
  --kind cover-letter --data /temporario/cover-letter.json \
  --output /caminho/jobs-applications/generated/empresa/vaga/cover-letter-IDENTIFICADOR.pdf --max-pages 1
```

4. O helper cria HTML intermediário, executa `weasyprint --encoding utf-8`, conta páginas usando `LC_ALL=C pdfinfo`, e reduz fontes progressivamente se houver excesso. Corpo de 10,5pt não fica menor que 9,5pt. Nome e contatos mantêm tamanho. O limite explícito do usuário prevalece sobre o padrão.
5. Se o helper retornar `OVERFLOW`, a redução de fonte já foi tentada. Só agora encurte redundâncias ou remova pontos menos relevantes no JSON, preservando evidências essenciais, a veracidade e o formato das experiências. Não resuma livremente as descrições de empresas nem reduza os bullets abaixo de 35 palavras; mantenha o máximo de 65 palavras por bullet. Tente novamente. Não comprima indefinidamente nem entregue um PDF acima do limite.
6. Renderize as páginas com `pdftoppm -png PDF PREFIXO` numa pasta temporária e inspecione todas. Confira legibilidade, quebras, links, títulos isolados, sobreposição e cortes. Extraia o texto com `pdfplumber`, `pypdf` ou `pdftotext` e verifique acentos, leitura linear, contatos, datas, métricas e termos ATS. Uma contagem de páginas correta não substitui essa revisão.
7. Se uma versão precisar de correção, preserve-a e use outro identificador de arquivo. O helper recusa sobrescrita inclusive em caso de colisão concorrente. Após validar, apague JSON, imagens e demais intermediários que você criou; o HTML temporário do helper já é removido automaticamente. Mantenha os assets permanentes da skill. Em `generated/empresa/vaga/` na raiz do projeto, mantenha apenas os materiais finais versionados, sem subpastas por execução. Este fluxo gera PDFs; Markdown de entrevista só é criado pela skill separada, mediante pedido explícito. Preserve os materiais existentes.

Se faltar uma fonte completa para um novo caractere, confirme o resultado visual e a extração. As fontes Calibri extraídas dos originais são subconjuntos; Arial é fallback. Não declare identidade tipográfica quando uma substituição tiver sido necessária. Prefira uma fonte Calibri local licenciada completa, se disponível, mantendo a mesma família visual.
