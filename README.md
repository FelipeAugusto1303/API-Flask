# Produto API

Este é o modulo backend que será avaliado pelos professores da Puc-Rio da disciplina de **Desenvolvimento Full Stack Básico**, este modulo foi desenvolvido em Flask python e possui funcionalidades para criar, buscar e deletar produtos.

## Como executar

vá ate o diretório raiz e execute os seguintes comandos no terminal

```bash
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API basta executar:

```bash
(env)$ flask run --host 0.0.0.0 --port 5176
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte.

```bash
(env)$ flask run --host 0.0.0.0 --port 5176 --reload
```

Abra o [http://localhost:5176/#/](http://localhost:5176/#/) no navegador para verificar o status da API em execução.
