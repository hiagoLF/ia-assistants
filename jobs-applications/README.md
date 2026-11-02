# Candidaturas a vagas

Este projeto concentra a avaliação de vagas e a adaptação de currículos e cover letters de Hiago Leão. O único registro de candidatura são os arquivos de resume, cover-letter e interview em `generated/`. A preparação para entrevistas é uma etapa separada, usada por pedido explícito quando uma entrevista estiver marcada.

## Fluxo de trabalho

1. Envie o link ou a descrição da vaga. A skill `is-this-job-for-me` verifica aderência ao perfil, condições essenciais e instruções obrigatórias de candidatura.
2. Depois da avaliação, peça a preparação da candidatura. A skill `fit-resume-for-job` adapta o resume e as respostas do formulário; inclui cover letter quando solicitada ou exigida pela vaga.
3. A skill `build-resume-cover-letter-from-template` renderiza os PDFs a partir dos templates existentes, preservando layout, histórico e limites de páginas.
4. Quando houver entrevista marcada, peça explicitamente `$prepare-for-job-interview`. Essa skill gera um roteiro de prática específico para a etapa. Ela nunca é chamada automaticamente pelas outras skills.

Nenhuma candidatura é enviada automaticamente. Não são criados arquivos separados de acompanhamento, status ou avaliação de vagas.

## Skills locais

As quatro skills ficam em [.agents/skills/](.agents/skills/), com seus scripts, referências e assets. As três skills importadas substituem as instalações globais anteriores.

- [is-this-job-for-me](.agents/skills/is-this-job-for-me/SKILL.md): avalia compatibilidade, critérios eliminatórios, pendências, tecnologias e exigências da candidatura.
- [fit-resume-for-job](.agents/skills/fit-resume-for-job/SKILL.md): prepara conteúdo fiel ao perfil, com termos ATS sustentados por experiência real, perguntas agrupadas, PDFs e respostas de formulário.
- [build-resume-cover-letter-from-template](.agents/skills/build-resume-cover-letter-from-template/SKILL.md): transforma conteúdo preparado em PDFs selecionáveis usando os templates HTML, WeasyPrint e validação visual e textual.
- [prepare-for-job-interview](.agents/skills/prepare-for-job-interview/SKILL.md): prepara perguntas e sugestões de respostas em inglês para entrevista marcada, somente mediante solicitação explícita.

As regras permanentes de seleção e uso estão em [AGENTS.md](AGENTS.md).

## Perfil e decisões

Os critérios de avaliação foram mantidos: foco em React/React Native, remoto do Brasil, preferência por pagamento em USD e mínimo de US$4.000/mês ou US$48.000/ano; EUR é alternativa conforme a verificação cambial da skill. As demais condições e exceções estão na skill de avaliação.

A conversa, as perguntas e a documentação são em português. Os materiais da candidatura e da entrevista são em inglês, salvo instrução diferente ou exigência da vaga. Todas as perguntas necessárias de uma rodada são enviadas juntas.

As fontes do perfil estão em `.agents/skills/fit-resume-for-job/references/`. As transcrições originais são preservadas; novas informações precisam de autorizações separadas para uso atual e persistência futura. Correções autorizadas mais recentes prevalecem sobre o original.

## Organização dos arquivos

```text
jobs-applications/
├── README.md
├── AGENTS.md
├── .agents/skills/
│   ├── is-this-job-for-me/
│   ├── fit-resume-for-job/
│   ├── build-resume-cover-letter-from-template/
│   └── prepare-for-job-interview/
└── generated/<empresa-slug>/<vaga-slug>/
    ├── resume-IDENTIFICADOR.pdf
    ├── cover-letter-IDENTIFICADOR.pdf
    └── interview-IDENTIFICADOR.md
```

Os arquivos listados em `generated/` dependem do que foi solicitado. O Markdown de entrevista só é criado no fluxo explícito de preparação. Os quatro arquivos históricos da Tec2Cloud foram preservados com seus nomes originais.

Cada execução usa um identificador com data, hora, fuso `America/Bahia` e sufixo aleatório. Não há subpastas por execução nem sobrescrita de versões. Os limites padrão são duas páginas para resume e uma para cover letter; primeiro se ajusta a fonte até o mínimo legível, depois se encurta o texto quando necessário.

Todos os arquivos permanentes, incluindo referências pessoais, assets e materiais de `generated/`, devem fazer parte do repositório. Não há exclusões em `.gitignore`. JSON, HTML intermediário, imagens de revisão e caches são temporários e ficam fora do projeto.

## Geração dos PDFs

O renderer usa Python 3, WeasyPrint e Poppler (`pdfinfo`, `pdftoppm` e, opcionalmente, `pdftotext`). Consulte as [instruções de dependências](.agents/skills/build-resume-cover-letter-from-template/references/commands.md) e o [schema de entrada](.agents/skills/build-resume-cover-letter-from-template/references/input-schema.md).

Para obter caminhos inéditos, execute a partir da raiz:

```bash
python3 .agents/skills/fit-resume-for-job/scripts/new_run.py \
  --company "Empresa" --job "Frontend Engineer" --kind resume
```

Use `--kind cover-letter` para a carta. O modo `--kind interview` é reservado ao pedido explícito de preparação. O helper retorna caminhos; ele não gera documentos nem reserva os nomes. O renderer e a gravação do Markdown usam criação exclusiva para evitar sobrescrita.
