1. Andrii Liubashchenko
English: Worth being precise about "keeps keyboard focus inside", because it's slightly different from a JS focus trap.
In Chromium 141, a showModal() dialog with two buttons and a button on the page behind it: Tab went A, B, then out of the document (to the browser's own UI), then back to A. The page button was never reachable, but there is one stop outside the dialog per cycle.
For most users that's fine and expected. If a design spec says focus must never leave the dialog, that's the one gap native <dialog> leaves.
Portuguese: Vale ser preciso sobre "mantém o foco do teclado dentro", porque isso é um pouco diferente de um bloqueio de foco feito em JS.
No Chromium 141, em um diálogo aberto com showModal() com dois botões e um botão na página atrás dele: ao pressionar Tab, o foco passou por A, B, depois saiu do documento (para a interface do próprio navegador) e então voltou para A. O botão da página nunca ficou acessível, mas há uma parada fora do diálogo por ciclo.
Para a maioria dos usuários, isso é aceitável e esperado. Se uma especificação de design diz que o foco nunca deve sair do diálogo, essa é a única lacuna que o <dialog> nativo deixa.

1.1 Hiago
English: Agreed! That caveat deserves to be explicit: after reaching the last focusable element on the page, focus can move to the browser UI. This is part of the native, expected behavior of keyboard navigation in web applications.
Portuguese: Concordo! Essa ressalva merece ficar explícita: ao chegar ao fim dos elementos focáveis da página, o foco pode passar para a interface do navegador. Isso faz parte do comportamento nativo e esperado da navegação por teclado em aplicações web.

2. Irina Salmova
English: This is a good example of treating the browser as part of the component contract. The React wrapper should own the API and rendering decisions, while the platform owns the hard interaction rules: top layer, inert background, focus behavior, and dismissal. That boundary also makes code reviews clearer, because the custom logic has less room to accidentally reimplement accessibility.
Portuguese: Este é um bom exemplo de tratar o navegador como parte do contrato do componente. O wrapper em React deve ser responsável pela API e pelas decisões de renderização, enquanto a plataforma cuida das regras complexas de interação: camada superior, conteúdo de fundo inerte, comportamento do foco e fechamento. Essa divisão também deixa as revisões de código mais claras, porque a lógica personalizada tem menos espaço para reimplementar acidentalmente a acessibilidade.

2.1 Hiago
English: Yes! That separation makes code reviews clearer: the React component handles the API and rendering, while the browser takes care of native interaction behavior.
Portuguese: Sim! Essa divisão deixa a revisão mais clara: o componente React cuida da API e da renderização, enquanto o navegador assume os comportamentos nativos de interação.

3. Ali Asghar
English: Checking what the browser already provides before building custom components saves a lot of overhead. Native dialog handles accessibility and backdrops out of the box.
Portuguese: Verificar o que o navegador já oferece antes de criar componentes personalizados poupa bastante trabalho extra. O diálogo nativo já cuida da acessibilidade e dos fundos de sobreposição.

3.1 Hiago
English: Agreed! The browser often already provides the tools we need, and we may not even know it. Knowing those features can save a lot of work when building components.
Portuguese: Concordo! Muitas vezes o navegador já oferece as ferramentas de que precisamos, e a gente nem sabe. Conhecer esses recursos pode poupar bastante trabalho ao criar componentes.
