## Superheroes API
A Flask-based REST API for managing superheroes, their powers, and the relationships between them.

## FUNCTIONS 
This project allows you to:
-List all heroes or a single hero.
-List all powers or a single power.
-Update a power’s description.
-Create a hero-power association with a strength rating.

## Technologies Used
-Python 
-Flask-SQLAlchemy
-SQLite 


## REQUIREMENTS
1. Install dependencies
pip install -r requirements.txt

2. Set up the database
flask db init      
flask db migrate   
flask db upgrade    


3. Run the server
flask run
By default, the server will run at:
http://127.0.0.1:5000/

## Sample Requests
-Get all heroes -curl http://127.0.0.1:5000/heroes

## AUTHOR 
Morris Kamau 