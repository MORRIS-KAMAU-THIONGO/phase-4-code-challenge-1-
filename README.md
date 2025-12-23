## Superheroes API

A Flask-based REST API for managing superheroes, their powers, and the relationships between them.

This project allows you to:
-List all heroes or a single hero.
-List all powers or a single power.
-Update a power’s description.
-Create a hero-power association with a strength rating.

## Technologies Used

Python 3.x

Flask

Flask-SQLAlchemy

SQLite 

JSON for data transfer


2. Create and activate a virtual environment
python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Set up the database
flask db init       # Initialize migrations
flask db migrate    # Create migration scripts
flask db upgrade    # Apply migrations to the database

5. Run the server
flask run


By default, the server will run at:

http://127.0.0.1:5000/

🛣️ Available API Endpoints
Heroes

GET /heroes – Get a list of all heroes

GET /heroes/<id> – Get a specific hero by ID

Powers

GET /powers – Get a list of all powers

GET /powers/<id> – Get a specific power by ID

PATCH /powers/<id> – Update a power’s description

Hero Powers

POST /hero_powers – Create a hero-power association

📦 Sample Requests

Get all heroes

curl http://127.0.0.1:5000/heroes


Update a power

curl -X PATCH -H "Content-Type: application/json" \
-d '{"description":"New power description"}' \
http://127.0.0.1:5000/powers/1


Create a hero-power association

curl -X POST -H "Content-Type: application/json" \
-d '{"hero_id":1,"power_id":2,"strength":"Strong"}' \
http://127.0.0.1:5000/hero_powers

⚡ Notes

Ensure the database is migrated before running the server.

The API returns JSON responses for all endpoints.

Error handling is included for invalid requests or missing records.