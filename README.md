# Locar---Sistema-de-Gerenciamento-de-alugueis-de-Ve-culos
Projeto para estudo de python e tkinter para o curso da Fábrica de Software do Senac MS

A – VISÃO GERAL DO SISTEMA

O sistema de gerenciamento de locação traz de maneira fácil e intuitiva o controle dos veículos alugados na “Locar”. Sendo possível ter o controle tantos dos aluguéis, trazendo as informações dos clientes e do veículo locado, como ter o controle do estoque de veículos que estão disponíveis pra locação. 

B – ESPECIFICAÇÃO DOS REQUISITOS

O sistema terá um painel de controle de alugueis, onde terá acesso aos agendamentos já realizados, contendo as informações do contratante e seu histórico de locação, e da locação do veículo com informações como, local de retirada e devolução, datas e horas de retirada e devolução, quantidade e valores das diárias, valor total, informações do veículo, estado do veículo, ocorrências, serviço adicional e status do veículo. Ainda poderá ter um controle do seu estoque de veículos disponíveis para locação.

C – REQUISITOS FUNCIONAIS

RF01. Alterar reserva

Descrição: O usuário deseja alterar informações da reserva do veículo.

Entrada: Local de retirada e de devolução, data e hora de retirada e devolução, quantidade de diárias e serviço adicional.

Processo: O usuário altera as informações informadas acima.

Saída: O sistema exibe mensagem de Alterado com Sucesso. 


RF02. Cancelar reserva

Descrição: O usuário deseja cancelar a reserva de um veículo.

Entrada: O motivo do cancelamento.

Processo: O sistema verifica se a reserva obedece a regra de negócio de cancelamento da reserva, calcula os valores do reembolso, informa o usuário e altera o status da reserva.

Saída: O sistema exibe mensagem de Cancelado com Sucesso. 


RF03. Buscar reserva

Descrição: O usuário deseja buscar uma reserva no sistema.

Entrada: Número da reserva.

Processo: O sistema verifica se existe reserva com o número informado e retorna ao usuário.

Saída: O sistema exibe as informações da reserva. 


RF 04. Retirar veículo

Descrição: O usuário registra a retirada do veículo no sistema. 

Entrada: Local de retirada e de devolução, data e hora de retirada e devolução, quantidade e valores das diárias, formas de pagamento, informações do veículo, sendo placa, marca, transmissão, descrição, ano, tipo do combustível, número de portas e quilometragem e serviço adicional.

Processo: O sistema registra a retirada do veículo, valida a RN2 e altera o status do veículo para alugado.

Saída: O sistema exibe mensagem de Veículo Retirado com Sucesso.


RF 05. Devolver veículo

Descrição: O usuário registra a devolução do veículo. 

Entrada: Local de retirada e de devolução, data e hora de retirada e devolução, quantidade e valores das diárias, valor total, cartão de crédito, informações do veículo, sendo placa, marca, transmissão, descrição, ano, tipo do combustível, número de portas e quilometragem, ocorrências, sendo furto/roubo, sujeira, acidente ou outros e serviço adicional.

Processo: O sistema registra os dados de devolução e altera o status do veículo.

Saída: O sistema exibe mensagem de Veículo Devolvido com Sucesso.


RF 06. Registrar multa

Descrição: O usuário deseja registrar as multas do contratante referente as datas da locação.

Entrada: Nome do condutor, CNH, placa e modelo do veículo, informação da autuação, local, data, hora, valor da multa, vencimento da multa e forma de pagamento.

Processo: O sistema cadastra as informações e registra a cobrança para o contratante.

Saída: O sistema exibe a mensagem de Multa Registrada com Sucesso.


RF 07. Buscar veículos

Descrição: O usuário deseja buscar os veículos para o gerenciamento de estoque.

Entrada: Modelo do veículo

Processo: O sistema busca no banco de dados e retorna as informações do veículo.

Saída: O sistema exibe as informações do veículo buscado.


RF 08. Adicionar condutor

Descrição: O usuário adiciona um condutor extra para a reserva do veículo.

Entrada: Nome do condutor, CNH, CPF, endereço, e-mail e telefone.

Processo: O sistema registra as informações e adiciona o condutor extra. 

Saída: O sistema exibe a mensagem de Condutor Adicionado.


RF 09. Alterar veículo

Descrição: O usuário deseja alterar o veículo reservado, sendo de categoria semelhante ou diferente.

Entrada: Modelo do veículo, placa do veículo e descrição.

Processo: O sistema registra alteração do veículo, altera o status do veículo anterior para disponível e o do veículo atual para alugado.

Saída: O sistema exibe a mensagem de Alteração Realizada


RF 10. Realizar upgrade de veículo

Descrição: O usuário deseja realizar o upgrade para um veículo melhor da mesma categoria.

Entrada: Modelo do veículo, placa do veículo e descrição.

Processo: O sistema registra o upgrade do veículo e valida a RN5. 

Saída: O sistema exibe a mensagem Upgrade Realizado.


D – REQUISITOS NÃO FUNCIONAIS

-	Desempenho

O sistema deve responder à solicitação de ação do usuário dentro de um intervalo de 5 segundos.

-	Usabilidade

O sistema deve ter um layout intuitivo, que seja fácil de aprender e de utilizar.

-	Portabilidade

O sistema deve funcionar no sistema operacional Windows a partir da versão 8.0.


E – REGRAS DE NEGÓCIOS

RN1- Cancelamento da reserva

O reembolso de 100% do pré-pagamento será feito ao cliente, caso a reserva tenha sido cancelada 48 horas antes da data de retirada. Caso a reserva seja cancelada quando faltar menos de 48 horas para a retirada, o reembolso será de 50% do pré-pagamento.

RN2 - Retirada do veículo

Antes da retirada do veículo pelo cliente, ele deve passar por uma inspeção completa, sendo limpeza completa, manutenção realizada e tanque cheio.


RN3 - Devolução do veículo

O veículo deve ser devolvido nas mesmas condições em que estava quando o cliente recebeu. Caso haja qualquer mancha/sujeira excessiva e/ou danos internos e externos (incluindo cheiros fortes). Será cobrado a taxa de 40 reais para limpeza simples e 150 para limpeza completa, levando em conta a condição do veículo.
Em caso de roubo ou furto, se obedecer às regras do seguro escolhido pelo cliente no ato da reserva.

RN4 - Anulação do seguro

Se o cliente conduzir sob a influência de álcool ou drogas, utilizar o veículo alugado de qualquer outra forma negligente ou imprudente, ou quebrar as condições estabelecidas no Contrato de Locação, todas as coberturas de seguro aplicáveis serão consideradas nulas e este será totalmente responsável por todos os danos ao veículo, bem como perda de uso e quaisquer outros custos relacionados. 

RN5 – Upgrade de Veículo

Só será permitido realizar upgrade de veículos da mesma categoria.
