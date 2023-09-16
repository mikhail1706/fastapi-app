## FastAPi Application

### Alembic
**init**
```
alembic init migrations
```

**Create revision (migration)**
```
alembic revision --autogenerate -m "Database creation"
```

**Apply migration**
```
alembic upgrade ccec83715a06
```
---
### Celery 
```
celery -A tasks.tasks:celery_app worker --loglevel=INFO
```
### Flower
```
celery -A tasks.tasks:celery_app flower
```

### Pytest
```
pytest -v tests
```

run tests with print resutls
```
pytest -v -s tests/
```
