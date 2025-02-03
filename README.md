# Nome da API

## Django API for management of a autostore

A api foi construída usando Django Rest Framework, com autenticação em JWT, bem como utilizando ModelViewSets para criação de views.

Exemplo:
> Esta API permite realizar operações CRUD em um sistema de produtos genéricos

## Tecnologias utilizadas

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Docker](https://www.docker.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Redis](https://redis.io/)
- [Celery](https://docs.celeryproject.org/)

## Instalação

Clone o projeto no github

- pip freeze > requirements.txt
- docker compose build
- docker compose up -d
- docker compose exec web bash

# Dentro do container, gere as migrações

- python manage.py makemigrations
- python manage.py migrate
