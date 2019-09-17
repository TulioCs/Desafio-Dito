## Desafio Dito

<h2> 1 - Serviço de Autocomplete </h2>

O serviço deve conter uma API Coletora de dados e o mecanismo de
Autocomplete propriamente dito.

API Coletora

Você deverá construir uma API para coletar e armazenar os dados. Esta API deverá
receber informações de navegação dos usuários em um site. Um exemplo seria:
{
"event": "buy",
"timestamp": "2016-09-22T13:57:31.2311892-04:00"
}

Autocomplete
O mecanismo de autocomplete deve ser implementado e disponibilizado através de
uma API, contendo um campo de busca que deverá completar o nome dos eventos
a partir da segunda letra que o usuário digitar.

<h2> 2 - Manipulação de Dados </h2>
O objetivo é criar uma timeline de compras a partir dos eventos disponíveis neste
endpoint: https://storage.googleapis.com/dito-questions/events.json.
Você deve implementar uma função, em qualquer linguagem de programação, que
consuma esse endpoint e agrupe as compras pelo campo transaction_id. Cada
item da timeline deve representar uma compra em uma determinada loja e deve
conter uma lista com os produtos comprados. A timeline deve ser ordenada pelo campo timestamp na ordem decrescente.

## Ferramentas utilizadas na questão 1

- Flask
- flask_sqlalchemy
- flask_migrate
- flask_marshmallow
- marshmallow_sqlalchemy

## Como executar a solução da questão 1

```sh
export FLASK_APP=app
export FLASK_ENV=Development
export FLASK_DEBUG=True

flask run
```

#EndPoints

- http://localhost:5000/events mostra todos os eventos cadastrados
- http://localhost:5000/events/cadastrar cadastrar novos eventos
- http://localhost:5000/autocomplete/string_de_busca autocomplete

## Ferramentas utilizadas na questão 2

- Python3
- requests: biblioteca para fazer requisições HTTP em Python
- json: biblioteca para trabalhar com Json em Python

## Como executar a solução da questão 2

python3 main.py
