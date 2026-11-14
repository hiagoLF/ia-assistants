1. Michael Livesey
English: What causes the component to rerender? You need to be careful because if "items" isn't something observed or stateful by React, nothing will happen.

But yes, for derived values a direct calculation is better, and if heavy, wrapped in useMemo.
Portuguese: O que faz o componente renderizar de novo? É preciso ter cuidado, porque, se o React não acompanha "items" e esse valor não faz parte do estado, nada vai acontecer.

Mas sim, para valores derivados, é melhor calcular diretamente e, se o cálculo for pesado, usar useMemo.

1.1 Hiago
English: Good point, Michael. The example assumes `items` comes from props or state. Mutating a regular array outside of state won’t trigger a re-render on its own. If the calculation is expensive, `useMemo` can help skip recalculating it when the dependencies haven’t changed.
Portuguese: Boa observação, Michael. O exemplo parte de `items` vindo de props ou do estado. Alterar um array comum fora do estado não dispara uma renderização por si só. Se o cálculo for caro, `useMemo` pode ajudar a evitar recalculá-lo quando as dependências não mudam.

2. Favour Nwachukwu
English: I'd also watch for duplicated sources of truth. [**Hiago**](https://www.linkedin.com/in/hiago-leao/)

When the same information lives in multiple state variables, consistency becomes an extra responsibility.
Portuguese: Eu também ficaria de olho na duplicação de fontes de verdade. [**Hiago**](https://www.linkedin.com/in/hiago-leao/)

Quando a mesma informação fica em várias variáveis de estado, manter tudo consistente vira uma responsabilidade a mais.

2.1 Hiago
English: Well said, Favour. If the total is also stored in state, every change to a price or quantity means keeping both values in sync. Calculating the total from `items` keeps the items as the single source of truth.
Portuguese: Bem colocado, Favour. Se o total também fica no estado, cada mudança de preço ou quantidade precisa manter os dois valores em sincronia. Calcular o total a partir de `items` deixa os itens como a única fonte de verdade.

3. Irina Salmova
English: A nice side effect is that tests become simpler too. You verify the cart items and the rendered total together, instead of chasing an intermediate state update that only exists because of the Effect.
Portuguese: Um efeito colateral positivo é que os testes também ficam mais simples. Você verifica os itens do carrinho e o total exibido juntos, em vez de ter que acompanhar uma atualização intermediária de estado que só existe por causa do Effect.

3.1 Hiago
English: Good point, Irina! A test can change an item’s quantity and check that the updated quantity and total both appear on screen. That keeps the test focused on what someone sees when using the cart.
Portuguese: Boa observação, Irina! Um teste pode alterar a quantidade de um item e conferir se a nova quantidade e o total aparecem juntos na tela. Isso mantém o teste focado no que a pessoa vê ao usar o carrinho.
