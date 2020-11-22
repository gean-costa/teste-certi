![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

# Desafio Técnico de Software - CERTI

## Introdução
Olá, seja bem-vindo.

Esta aplicação foi desenvolvida como resolução do desafio técnico proposto em e-mail.

O teste consistia na seguinte proposta:

*Na linguagem de sua preferência, crie um servidor HTTP que, para cada requisição GET, retorne um JSON cuja chave extenso seja a versão por extenso do número inteiro enviado no path. Os números podem estar no intervalo [-99999, 99999]*.

*Exemplos*:

```bash
λ curl http://localhost:3000/1
{ "extenso": "um" }
```
```bash
λ curl http://localhost:3000/-1042
{ "extenso": "menos mil e quarenta e dois" }
```
```bash
λ curl http://localhost:3000/94587
{ "extenso": "noventa e quatro mil e quinhentos e oitenta e sete" }
```

## Informações gerais
O repositório da aplicação está disponível no [Github](https://github.com/gean-costa/teste-certi), em modo privado e compartilhado com o usuário "seletivo-certi-cdm", conforme solicitado.

Esta foi desenvolvida na liguagem Python (versão 3.8.5) por meio do microframework [Flask](https://flask.palletsprojects.com/en/1.1.x/). Para mais detalhes das bibliotecas utilizadas, consulte o arquivo ```requirements.txt```.

## Estrutura da aplicação
```bash
├── app.py
├── functions.py
├── num_dict.py
├── docker-compose.yml
├── Dockerfile
├── README.md
├── requirements.txt
├── scan_api
│   ├── scanapi.yaml
├── scanapi.conf
├── templates
│   └── tests-report.html
└── tests
    ├── __init__.py
    └── test_routes.py
```

## Deployment
Para rodar a aplicação na sua máquina, recomendamos a criação de um ambiente virtual para evitar possíveis problemas com as versões das bibliotecas utilizadas e suas dependências. Para isso, siga os seguintes passos:
```bash
> python -m venv NOME_ENV
```
```bash
> source NOME_ENV/bin/activate
```
```bash
> pip install -r requirements.txt
```
```bash
> flask run --host=localhost --port=3000
```
Com isso, a aplicação será executada no endereço http://localhost:3000/ e, caso queira mudar o endereço do host e da porta utilizada, basta informar no momento da execução, mudando os parâmetros acima conforme desejar.

Entretanto, se você possuir o Docker instalado, é possível também rodar a aplicação por meio de um container, cuja imagem está disponível [aqui](). Após o download, execute em seu terminal:
```bash
>
```

Caso opte por não fazer o download da imagem, você pode rodar a aplicação criando o container com o seguinte comando:
```bash
> docker-compose up
```
No caso da aplicação ser executada no Docker, o endereço será http://0.0.0.0:3000/ que tomaremos por padrão daqui pra frente.

## Principais Endpoints

| endpoint | descrição |
|----------|-----------|
|/home| Apresentação e informações gerais/documentação da aplicação. |
|/extenso/{num}| Gera a versão por extenso do paramêtro **{num}**. Por definição, **{num}** deve ser um número inteiro entre [-9999,99999]. Caso não seja, será retornada uma mensagem de erro. |
|/scanapi| Apresentação do report gerado pela execução dos testes usando a ferramenta ScanAPI (mais informações sobre a mesma a seguir).|

## Testes
Foram implementados dois conjuntos de testes, utilizando [Pystest](https://docs.pytest.org/en/stable/) e a [ScanAPI](https://scanapi.dev) (uma ferramenta para testes de integração e geração de reports), localizados nos diretórios ```tests/``` e ```scan_api/```, respectivamente.

Para executar os testes do Pytest, execute o comando:
```bash
> pytest -v
```

Para executar os testes da ScanAPI, execute o comando:
```bash
> scanapi run scan_api/scanapi.yaml
```
Para os testes com a ScanAPI, será gerado um report destes em um aquivo chamado ```tests-report.html```, que poderá ser acessado pelo endpoint ```/scanapi```.

## Exemplos de uso
```bash
> curl http://0.0.0.0:3000/extenso/0
{
  "extenso": "zero"
}
```
```bash
> curl http://0.0.0.0:3000/extenso/10
{
  "extenso": "dez"
}
```
```bash
> curl http://0.0.0.0:3000/extenso/-19
{
  "extenso": "menos dezenove"
}
```
```bash
> curl http://0.0.0.0:3000/extenso/73
{
  "extenso": "setenta e tres"
}
```
```bash
> curl http://0.0.0.0:3000/extenso/100
{
  "extenso": "cem"
}
```
```bash
> curl http://0.0.0.0:3000/extenso/110
{
  "extenso": "cento e dez"
}
```
```bash
> curl http://0.0.0.0:3000/extenso/-666
{
  "extenso": "menos seiscentos e sessenta e seis"
}
```
```bash
> curl http://0.0.0.0:3000/extenso/1073
{
  "extenso": "mil e setenta e tres"
}
```
```bash
> curl http://0.0.0.0:3000/extenso/-99100
{
  "extenso": "menos noventa e nove mil e cem"
}
```
