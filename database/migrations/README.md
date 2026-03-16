# Alembic Migrations

Initialize migration environment:

```bash
alembic init database/migrations
alembic revision --autogenerate -m "initial schema"
alembic upgrade head
```
