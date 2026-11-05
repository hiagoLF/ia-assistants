---
name: prepare-for-job-interview
description: Preparar Hiago Leão para uma entrevista de emprego marcada, com perguntas e sugestões de respostas em inglês. Usar somente por pedido explícito; não integrar automaticamente à candidatura.
---

# Preparação para entrevista

Use somente quando o usuário pedir explicitamente a preparação para uma entrevista marcada. A avaliação da vaga, geração de currículo ou notícia de agendamento não autoriza acionar esta skill automaticamente.

Converse em português e produza o material em inglês, salvo instrução diferente. Aproveite o contexto da candidatura e os dados já fornecidos.

## Contexto e fontes

Leia [resume-original.md](../../../references/resume-original.md) e [cover-letter-original.md](../../../references/cover-letter-original.md), na pasta `references/` da raiz do projeto. Correções explícitas mais recentes prevalecem. Para Knowledge Paths, a métrica correta é consumo de materiais 5× maior.

Consulte a descrição da vaga e o currículo enviado em `generated/<empresa>/<vaga>/` na raiz do projeto. Se houver versões diferentes, identifique a enviada pelo contexto ou pergunte; não presuma que seja a mais recente. Abra links fornecidos e use fontes oficiais para informações atuais da empresa. Não alegue ter lido uma fonte inacessível.

Reúna todas as perguntas necessárias em uma única rodada numerada em português, conforme [grill-me](../grill-me/SKILL.md): empresa e vaga, etapa, data e fuso, idioma, formato, entrevistadores conhecidos e assuntos que deseja praticar. Pergunte só o que faltar e for relevante; não bloqueie a preparação por detalhes opcionais desconhecidos. Se o agendamento não estiver confirmado, esclareça antes de produzir o material. Use dessa skill apenas as regras de entrevista agrupada e autorização; perguntas sobre formulário e cover letter pertencem à candidatura.

Para experiências novas, obtenha permissões separadas de uso na preparação atual e persistência nas referências. Não repita autorizações já concedidas para o mesmo escopo.

## Material de prática

Agrupe em **Screening interview** e **Technical interview**, priorizando a etapa marcada e os requisitos da vaga.

No screening, cubra apresentação, motivação, experiência relevante, trabalho remoto e perguntas para a empresa. Para informações pessoais pendentes, sugira uma estrutura de resposta.

Na parte técnica, inclua fundamentos, cenários e trade-offs das tecnologias e responsabilidades da vaga, além de aprofundamentos das realizações citadas no currículo enviado. Diferencie respostas conceituais de relatos pessoais. Use o formato STAR para questões comportamentais. As perguntas são sugestões de prática, não previsões garantidas da empresa.

## Saída e histórico

Execute `python3 .agents/skills/fit-resume-for-job/scripts/new_run.py --company EMPRESA --job VAGA --kind interview` a partir da raiz do projeto (ou use o caminho absoluto do script). Salve no caminho retornado, `generated/<empresa-slug>/<vaga-slug>/interview-IDENTIFICADOR.md`, com criação exclusiva (`open(..., 'x')`) e sem sobrescrever versões. Nunca salve artefatos na pasta da skill nem crie subpastas por execução.

O único registro de candidatura são os arquivos de resume, cover-letter e interview em `generated/`; não crie arquivos separados de acompanhamento ou status. Ao concluir, forneça o link do Markdown e as pendências que precisam ser confirmadas antes de usar as respostas.
