# Destaque

A proposta desse código é bem longa, por isso deixarei ela no final, mas em resumo:

> Fazer duas estruturas diferentes, uma para cliente e outra para documentos, separadas em dois vetores e interligadas por um código. Cada cliente poderia ter uma quantidade n de documento, e cada documento precisa estar atrelado em um cliente. E o menu propõe algumas funções de manipulação desse pequeno banco de dados.

Aqui, como diz a proposta, era pra ser usado dois vetores, porém conversando com a professora propus o uso de um dicionário para o cadastro de documentos e, como ela ainda não tinha ensinado o uso deste, ela aceitou me deixar tentar.

O maior desafio aqui foi de fato aprender a usar o dicionário e interligar tudo. O programa é bem extenso para o padrão que seguiamos, então, além de tudo, tive que planejar, escrever e corrigir um código mais longo do que estava acostumado.

 (E sim, em Estrutura de Decisão no 1º Semestre eu uso o dicionário para resolver um exercício, porém aquele foi utilizado muita ajuda de IA porque eu queria achar uma forma melhor de fazer aquele código. Aquela lista foi a última em que fiz algo do tipo, nas outras me restringi a resolver os exercícios com os recursos que me foram disponibilizados.)

## Lógica Utilizada

Como precisava que cada documento estivesse relacionado à um cliente através do `.cod_cli`, quando um cliente era gerado, o código dele era utilizado para criar uma chave dentro do dicionário que armazenava os documentos, facilitando o acesso de todos os documentos para cada cliente.

O código de cada cliente era tirado de um vetor com range(1000,2000) e o número de cada documento de um vetor com range(200, 2200) (aqui eu deixo 2000 números disponíveis porque limito a geração automática de até 2 documentos para cada cliente, o qual limitei a no máximo 1000); o que adicionava o desafio de quando um cliente ou documento fosse excluído, seu código poderia ser disponibilizado para uso novamente e em sequência.

Também é importante dizer que pelo fato da entrada de dados (o cadastro de clientes e documentos) ser manual, era muito trabalhoso o teste da cada função, então, para facilitar os testes, fiz uma função para cadastrar n quantidade de clientes com dados e documentos aleatórios.

## Proposta do Exercício:

Elabore duas estruturas, como é apresentado a seguir:
| CLIENTE  | DOCUMENTOS |
|----------|------------|
| cod_cli*  | num_doc    |
| nome     | cod_cli*    |
| fone     | dia_venc   |
|          | dia_pag    |
|          | valor      |
|          | juros      |

*Relacionado

* Sabe-se que um documento só pode ser cadastrado para um cliente que já exista.

* Considere que podem existir, no máximo, 15 clientes e 30 documentos. Crie um vetor para clientes e outro para documentos.

* Crie um menu para a realização de cada uma das operações especificadas a seguir:

** SISTEMA GERENCIADOR DE CLIENTES E DOCUMENTOS **

1. Cadastrar clientes
2. Relatório de clientes
3. Cadastrar documentos
4. Relatório de documentos
5. Excluir clientes sem documentos
6. Excluir documentos individuais pelo número
7. Excluir documentos por cliente
8. Excluir documentos por período
9. Alterar as informações dos clientes
10. Mostrar o total de documentos de determinado cliente
11. Sair

Qual opção deseja?

.................................................................................................

Para cada item do menu, desenvolva uma função.

A seguir são apresentados os detalhes de implementação de cada opção do menu:

* Cadastrar clientes — não pode existir mais que um cliente com o mesmo código.

* Relatório de clientes - listar todos os clientes cadastrados.

* Cadastrar documentos — ao cadastrar um documento, se o dia de pagamento for maior que o dia de vencimento, calcular o campo ‘juros’ do registro documentos (5% sobre o valor original do documento).

* Relatório de documentos - listar todos os documentos cadastrados.

* Excluir clientes — um cliente só poderá ser excluído se não existir nenhum documento associado a ele.

* Excluir documentos individuais — por meio de seu número. Caso o documento não exista, o programa deverá mostrar a mensagem "Documento não encontrado".

* Excluir documentos por cliente — o programa deverá informar o código do cliente e excluir todos os seus documentos. Caso o cliente não exista, deverá mostrar a mensagem "Cliente não encontrado".

* Excluir documentos por período — o programa deverá informar o dia inicial e o dia final e excluir todos os documentos que possuam data de vencimento nesse período.

* Alterar as informações sobre os clientes — só NÃO altere o código do cliente.

* Mostrar o total de documentos de determinado cliente.