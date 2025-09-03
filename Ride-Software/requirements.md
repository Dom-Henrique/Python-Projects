# Requirements of project

## 1. Cadastro do Usuário
- Nome completo;
- E-mail deve ser único;
- Informar se deu certo ou não.

***Dados de entrada: nome completo, e-mail e senha.***

## 2. Login
- Somente usuário logados podem executar os outros serviços.

## 3. Cadastro de Carona
- Usuário pode cadastrar carona;
- Cada carona pertence a UM ÚNICO USUÁRIO;

***Dados de entrada: Local de origem, destino, data, horário, vagas e valor por vaga.***

## 4. Listar caronas
- Exibir caronas com vagas disponíveis

***Dados de saída: nome do motorista, origem, destino, data, horário, vagas e valor por vaga.***

## 5. Listar caronas (origem e destino)
- Usuário insere ORIGEM e DESTINO;
- Sistema exibe os mesmos dados da 4° função.

## 6. Reservar carona
- Usuário reserva carona;
- Reduz uma vaga da carona;
- Quando não há vagas, avisar ao usuário.
***Dados de entrada: e-mail do motorista, data.***

## 7. Cancelar reserva
- Opção de cancelamento de reserva;
- Quando cancelada, a vaga volta a ficar disponível

## 8. Remover reserva
- Retira os dados inseridos;
- Informa ao usuário.

## 9. Detalhes da carona
- Exibe todos os detalhes das caronas;
- Busca pore-mail e data da carona.

***Dados de entrada: e-mail do motorista, data.***
***Dados de saída: origem, destino, horário, valor, vagas restantes e passageiros.***

## 10. Log Out
- Sai e fecha o programa.