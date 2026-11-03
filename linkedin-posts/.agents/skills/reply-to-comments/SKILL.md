---
name: reply-to-comments
description: Registrar comentários de posts do LinkedIn em inglês e português, sugerir respostas em português no chat e salvar as respostas bilíngues após confirmação ou orientação do usuário. Use quando o usuário colar comentários recebidos e indicar o post ou continuar uma conversa já registrada.
---

# Responder comentários

Mantenha a conversa com o usuário em português. Registre comentários e respostas em `posts/<topic-slug>/comments.md`, junto ao post correspondente. Não publique respostas no LinkedIn.

## Identificar o post e registrar comentários

1. Aceite nome, tema ou caminho para identificar o post. Leia seu `post.txt` e o `comments.md` existente, se houver. Se a identificação for ambígua ou o post não for encontrado, pergunte antes de criar ou alterar arquivos.
2. Para cada mensagem recebida, identifique autor, texto original e, quando houver, a conversa à qual pertence. Use `Autor desconhecido` quando o nome não tiver sido informado. Se não estiver claro a qual comentário principal uma continuação pertence, pergunte antes de registrá-la.
3. Verifique duplicatas dentro do mesmo post comparando autor e texto original com ambas as versões registradas. Ignore apenas diferenças de espaços e quebras de linha. Não descarte automaticamente textos apenas semelhantes: sinalize a possível repetição. Quando textos coincidirem e houver autor desconhecido, pergunte se são o mesmo comentário antes de inserir ou descartar.
4. Insira apenas mensagens novas. Preserve o texto recebido no campo de seu idioma e traduza fielmente para o outro, preservando sentido, emojis, código e identificadores. Se o idioma original não for inglês nem português, mantenha também um campo `Original (<idioma>):` para preservar o texto recebido e permitir a comparação futura.
5. Numere comentários principais na ordem recebida: `1`, `2`, `3`. Dentro de cada comentário, numere todas as mensagens seguintes na ordem recebida: `1.1`, `1.2`, `1.3`, independentemente de quem fala. Não crie níveis como `1.2.1`. Preserve números e conteúdo existentes; acrescente mensagens sem renumerar o histórico.

## Sugerir respostas no chat

- Apresente em uma única rodada os comentários pendentes, identificados pelo número e pelo autor, mostrando somente a versão em português de cada comentário.
- Para cada um, apresente uma sugestão de resposta somente em português. Use o contexto do post e da conversa para responder ao que a pessoa escreveu; não sugira tons nem peça que o usuário escolha um tom.
- Peça que o usuário confirme as sugestões ou indique, numeradamente, as respostas ou alterações desejadas. Aceite uma confirmação para todas. Se a intenção de uma confirmação parcial não estiver clara, pergunte apenas sobre os itens ambíguos; mantenha os demais pendentes.
- Comentários que já tenham resposta registrada de Hiago após a última mensagem recebida ficam fora dessa rodada, salvo pedido de revisão. Novas mensagens recebidas na mesma conversa podem exigir nova resposta.
- Mantenha sugestões não confirmadas apenas no chat. O registro dos comentários recebidos não depende da aprovação das respostas.

## Escrever e salvar respostas

- Cada versão de cada resposta de Hiago deve ter **no mínimo 20 e no máximo 60 palavras**, excluindo número, autor e rótulos dos campos. Use apenas o tamanho necessário dentro desse intervalo; não preencha até o máximo. O limite não se aplica aos comentários recebidos nem às traduções desses comentários.
- Conte as palavras de cada versão antes de apresentar ou salvar uma resposta. Para uma contagem consistente, separe o texto por espaços em branco, por exemplo com `len(texto.split())` em Python.
- Escreva respostas claras, naturais e adequadas ao contexto. Não invente experiências, opiniões, resultados ou informações pessoais de Hiago. Pergunte quando a resposta depender de informação pessoal ausente. Verifique documentação oficial quando houver dúvida técnica ou informação dependente de versão.
- Após a confirmação da sugestão, salve-a em português e adapte-a para inglês natural com o mesmo sentido. Se o usuário fornecer uma resposta alternativa ou pedir uma alteração clara, isso autoriza sua aplicação sem outra rodada de aprovação. Ajuste a redação para respeitar o intervalo de 20 a 60 palavras em cada idioma; se isso exigir perder um sentido essencial ou decidir uma intenção incerta, apresente uma alternativa em português no chat e aguarde confirmação.
- Registre respostas como mensagens de `Hiago` no comentário correspondente. Não inclua status de rascunho, publicação ou aprovação, nem outros controles de publicação.
- Ao revisar uma resposta existente, altere suas duas versões no mesmo número. Uma nova mensagem da conversa recebe o próximo número disponível.
- Preserve conteúdo não relacionado. Depois de salvar, mostre no chat as respostas salvas somente em português, com seus números, e forneça um link para `comments.md`.

## Formato do arquivo

Use blocos separados por linhas em branco, com a numeração escrita literalmente. Cada bloco contém autor e versões nos dois idiomas, sem formatação de lista que altere a numeração exibida. Por exemplo:

```text
1. Maria
English: Thanks for explaining this!
Portuguese: Obrigada por explicar isso!

1.1 Hiago
English: Glad it helped, Maria!
Portuguese: Que bom que ajudou, Maria!

1.2 Maria
English: Does this also work on Android?
Portuguese: Isso também funciona no Android?

2. Autor desconhecido
English: Great example!
Portuguese: Ótimo exemplo!
```

Use `English:` e `Portuguese:` também para mensagens de Hiago. Não crie `comments.md` vazio nem dados de exemplo em pastas de posts: crie o arquivo quando houver comentários reais para registrar.
