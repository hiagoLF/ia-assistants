# Entrada do renderer

JSON UTF-8, sem HTML. Strings são escapadas antes da renderização. Campos textuais aceitam string ou lista de objetos `{ "text": "...", "bold": true, "italic": true }`, exceto `achievements`, que usa strings simples. Use segmentos quando for necessário manter os destaques do original. Quebras de linhas são calculadas pelo renderer.

Campos comuns obrigatórios:

```json
{
  "name": "Nome",
  "email": "email@example.com",
  "phone": "+55 ...",
  "linkedin": "linkedin.com/in/perfil",
  "location": "Bahia, Brazil"
}
```

Resume acrescenta `headline`, `summary`, `jobs`, `education`, `courses`, `languages`. Os três últimos são listas de campos textuais. Cada item de `jobs` contém:

```json
{
  "title": "Cargo histórico verdadeiro",
  "company": "Empresa",
  "location": "Cidade, Brazil (remote)",
  "dates": "11/2022 – Present",
  "description": "Descrição original da empresa, com apenas ajustes pontuais de palavras-chave comprovadas; omitir se ausente no original",
  "achievements": ["Bullet completo de 35 a 65 palavras: descrição do que foi feito, seguida dos resultados e métricas confirmados, com as tecnologias ao final, no estilo do currículo original."],
  "skills": "React, React Native",
  "body_font": "roboto"
}
```

`body_font` pode ser `roboto` (padrão, como MB Labs/Elleven) ou `calibri` (como UFBA). A data de término e o status atual da ocupação vêm das referências, sem inferir mudanças.

Em resumes adaptados, conte as palavras de cada string de `achievements` por espaços, incluindo as tecnologias e sem o marcador. Cada item deve ter de 35 a 65 palavras e seguir a ordem o que foi feito → resultados e métricas → tecnologias. Use resultado qualitativo confirmado quando não houver métrica numérica. Não reformule livremente `description`: preserve o texto original, permitindo apenas ajustes pontuais de palavras-chave sustentados pelos fatos. Essas regras são verificadas na preparação do conteúdo; o renderer não valida a redação nem a contagem de palavras. As fixtures históricas permanecem intactas.

Cover letter acrescenta `salutation`, `paragraphs` (lista de parágrafos textuais), `closing`. A assinatura usa `name`. Os fixtures `assets/source-*.json` demonstram a estrutura completa, mas seu texto é histórico e não serve como fonte de verdade atualizada.

Antes da geração, aplique às strings as correções autorizadas das referências; especialmente não copie a métrica antiga da fixture de cover letter.
