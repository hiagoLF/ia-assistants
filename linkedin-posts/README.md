# LinkedIn Programming Posts

Projeto para criar posts originais sobre programação para o LinkedIn, com foco em JavaScript, TypeScript, React e React Native para desenvolvedores iniciantes e intermediários.

O post e a sugestão de imagem são preparados primeiro no idioma do usuário, com português como padrão. Depois da validação e do pedido do usuário, ambos são adaptados para inglês natural. As imagens geradas usam texto em inglês. A conversa segue o idioma do usuário.

## Como usar

- Peça um post ou use `$create-linkedin-post`, informando o tema. A skill apresenta no chat um texto de até 300 palavras e uma sugestão de imagem para revisão, sem salvar rascunhos nem gerar a imagem. Valide o conteúdo e peça a versão em inglês quando estiver pronto. Somente o post final em inglês é salvo; a sugestão de imagem continua apenas no chat.
- Peça a imagem ou use `$create-linkedin-image`, informando o tema do post. A skill gera uma imagem minimalista em inglês com o gradiente definido pelo projeto.

As skills ficam em `.agents/skills/`. As regras gerais ficam em `AGENTS.md`.

## Organização

Cada tema tem sua própria pasta, com nome em inglês e kebab-case:

```text
posts/
  javascript-filter/
    post.txt
    image.png
```

`post.txt` contém apenas a versão final do post em inglês, em texto puro, com quebras de linha quando necessário, sem Markdown nem instruções de revisão. Rascunhos para revisão e sugestões de imagem, inclusive em inglês, ficam apenas no chat. Somente a imagem final é salva como `image.png`, quando solicitada.
