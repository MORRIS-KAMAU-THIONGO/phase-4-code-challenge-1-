# phase-4-code-challenge-1-

# Superheroes API

## Author
Morris Thiongo

## Description
A Flask REST API for managing heroes and their superpowers.

## Setup
```bash
-pip install -r requirements.txt
-flask db upgrade
-python seed.py
-python run.py

## Routes
-GET /heroes
-GET /heroes/:id
-GET /powers
-GET /powers/:id
-PATCH /powers/:id
-POST /hero_powers

## Technologies
-Flask
-SQLAlchemy
-Flask-Mail