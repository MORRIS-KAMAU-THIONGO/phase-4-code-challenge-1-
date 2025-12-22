# Superheroes API

A Flask REST API for managing heroes, powers, and hero-power associations.

## Setup

```bash
pip install -r requirements.txt

# Initialize migrations
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# Seed the database
python server/seed.py

# Run the server
python server/app.py
```

## Routes
- GET /heroes
- GET /heroes/:id
- GET /powers
- GET /powers/:id
- PATCH /powers/:id
- POST /hero_powers
