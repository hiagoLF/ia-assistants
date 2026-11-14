1. Marina Iatsuk
English: TypeScript can only help after untrusted JSON crosses the boundary. Treating API responses as unknown, validating them once, and passing only parsed data deeper into the app keeps the rest of the code honest
Portuguese: O TypeScript só pode ajudar depois que o JSON não confiável atravessa essa fronteira. Tratar as respostas da API como unknown, validá-las uma vez e passar apenas os dados validados para as camadas internas da aplicação mantém o restante do código coerente com os tipos.

1.1 Hiago
English: Exactly, Marina! Centralizing validation at the boundary also avoids scattering checks across components. That way, the inner layers receive validated data, and an invalid response can be handled before it reaches the UI.
Portuguese: Exatamente, Marina! Centralizar essa validação na entrada também evita espalhar verificações pelos componentes. Assim, as camadas internas recebem dados validados, e uma resposta inválida pode ser tratada antes de chegar à interface.
