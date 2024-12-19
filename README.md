# API Blog Pessoal
Este projeto é uma **API RESTful** para uma plataforma de blog pessoal. A API permite criar, ler, atualizar e excluir artigos do blog, implementando as operações básicas de **CRUD**. Trata-se de uma aplicação prática para demonstrar o uso do **FastAPI**, **SQLAlchemy** e **PostgreSQL** como banco de dados.

## Funcionalidades Principais
- **Listagem de Artigos**: Endpoint para retornar uma lista de artigos, com possibilidade de filtros (data de publicação e tag).
- **Exibição de Artigo Único**: Endpoint para retornar um único artigo com base no seu ID.
- **Publicação de Artigo**: Endpoint para criar novos artigos com título e conteúdo.
- **Atualização de Artigo**: Endpoint para atualizar os dados de um artigo existente a partir do seu ID.
- **Exclusão de Artigo**: Endpoint para excluir um artigo através do seu ID.

## Tecnologias Utilizadas
- **FastAPI**: Framework performático para a construção de APIs em Python.
- **SQLAlchemy**: ORM para interação com o banco de dados de forma orientada a objetos (POO).
- **PostgreSQL**: Banco de dados relacional para armazenar os artigos.
- **Pydantic**: Para a validação dos dados de entrada e saída.
