# Monitoramento de Produção

## Descrição

Este é um projeto simples de API desenvolvido em **Python** com **Flask**, que registra e consulta a produção por turno de trabalho. Feito para aplicações básicas de controle e monitoramento em ambientes industriais.

## Funcionalidades

- Registrar a quantidade de produção em determinado turno.
- Consultar os registros de produção realizados.

## Tecnologias Utilizadas

- **Python 3**
- **Flask**
- **Postman** (para testes das requisições)

## Como Executar o Projeto

1. Clone este repositório:

   ```bash
   git clone https://github.com/Le-dev24/monitoramento_producao.git
   ```

2. Acesse a pasta do projeto:

   ```bash
   cd monitoramento_producao
   ```

3. Instale as dependências:

   ```bash
   pip install flask
   ```

4. Execute o servidor:

   ```bash
   python monitoramento.py
   ```

5. O servidor estará rodando em:

   ```
   http://127.0.0.1:5001/
   ```

## Exemplos de Uso

### Registrar Produção (POST)

Endpoint:

```
POST /registrar_producao
```

Exemplo de corpo da requisição (JSON):

```json
{
  "turno": "manha",
  "quantidade": 150
}
```

### Consultar Registros (GET)

Endpoint:

```
GET /registros
```

## Testando a API

Você pode usar o **Postman** ou **curl** no terminal para testar as requisições.

Exemplo com curl:

```bash
curl -X POST http://127.0.0.1:5001/registrar_producao -H "Content-Type: application/json" -d "{\"turno\": \"manha\", \"quantidade\": 150}"
```

Exemplo GET:

```bash
curl http://127.0.0.1:5001/registros
```

## Autor

Letícia Cardoso Ramos

