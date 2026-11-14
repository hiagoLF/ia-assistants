1. Andrii Liubashchenko
English: The same mechanism works in your favor outside lists. A notes field that should start empty when you switch from Ana to Bruno can just get key={user.id}.
Checked in React 19.3: without the key, "Send proposal" stayed in the field after switching users. With the key, React mounted a fresh component and the field was empty. No effect to reset state needed.
Portuguese: O mesmo mecanismo funciona a seu favor fora das listas. Um campo de notas que deve começar vazio ao trocar de Ana para Bruno pode simplesmente receber key={user.id}.
Verifiquei no React 19.3: sem a key, "Send proposal" permaneceu no campo após trocar de usuário. Com a key, o React montou um novo componente e o campo ficou vazio. Sem precisar de um effect para redefinir o estado.

1.1 Hiago
English: Good point, Andrii! The key also lets you define when state should reset. In this example, placing it on the component that holds the notes makes switching users recreate that component with its initial state.
Portuguese: Boa observação, Andrii! A key também permite definir quando o estado deve ser reiniciado. Nesse exemplo, colocá-la no componente que mantém as notas faz a troca de usuário recriar esse componente com o estado inicial.
