# Comandos pesquisados e testados

Pesquisa e teste executados em subagente em 01/11/2026, antes da criação da skill. Ambiente validado: WeasyPrint 69.0, Pango 1.58.2, Python 3.14.6 e pdfinfo 26.05.0. Um HTML A4 de teste resultou em 2 páginas, com fontes embutidas, acentos e bullets extraíveis e página visualmente inspecionada. Nenhuma instalação foi necessária, portanto os comandos de instalação foram documentados, não executados.

Documentação oficial consultada:

- [WeasyPrint: instalação e CLI](https://doc.courtbouillon.org/weasyprint/latest/first_steps.html)
- [Fórmula Homebrew do WeasyPrint](https://formulae.brew.sh/formula/weasyprint)

## Verificação e instalação quando necessário

```bash
command -v weasyprint
weasyprint --version
command -v pdfinfo
pdfinfo -v
```

Se o executável estiver ausente no macOS com Homebrew:

```bash
brew install weasyprint
brew install poppler
```

Execute só a instalação que faltar. Instalações de sistema exigem as permissões normais do ambiente. Não reinstale um comando já funcional nem apresente a instalação como testada neste ambiente. Em outros sistemas, consulte as instruções oficiais específicas antes de instalar dependências nativas; a CLI de geração permanece a mesma.

## Conversão e contagem verificadas

Defina as variáveis como caminhos reais; a pasta de trabalho deve ser temporária e gravável.

```bash
mkdir -p "$WORK_DIR/cache"
XDG_CACHE_HOME="$WORK_DIR/cache" weasyprint \
  --encoding utf-8 "$INPUT_HTML" "$OUTPUT_PDF"
LC_ALL=C pdfinfo "$OUTPUT_PDF" | awk '/^Pages:/ {print $2}'
```

O cache gravável evita os avisos de Fontconfig observados no sandbox. O helper usa esses comandos por listas de argumentos, sem interpolação de shell, e verifica os códigos de saída. O PDF é produzido primeiro num local temporário e publicado apenas quando atende ao limite de páginas. A CLI do WeasyPrint, usada diretamente, pode sobrescrever arquivos; para candidaturas, use o helper, que publica com criação exclusiva.

O usuário não precisa ter `pdftotext` se houver `pdfplumber` ou `pypdf` disponível no runtime. `pdftoppm` e `pdfinfo` fazem parte do Poppler.
