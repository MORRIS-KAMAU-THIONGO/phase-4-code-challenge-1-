# server/app.py
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/heroes')
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([
        {
            "id": h.id,
            "name": h.name,
            "super_name": h.super_name
        } for h in heroes
    ]), 200


@app.route('/heroes/<int:id>')
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404

    hero_powers_list = []
    for hp in hero.hero_powers:
        hero_powers_list.append({
            "id": hp.id,
            "hero_id": hp.hero_id,
            "power_id": hp.power_id,
            "strength": hp.strength,
            "power": {
                "id": hp.power.id,
                "name": hp.power.name,
                "description": hp.power.description
            }
        })

    return jsonify({
        "id": hero.id,
        "name": hero.name,
        "super_name": hero.super_name,
        "hero_powers": hero_powers_list
    }), 200


@app.route('/powers')
def get_powers():
    powers = Power.query.all()
    return jsonify([
        {
            "id": p.id,
            "name": p.name,
            "description": p.description
        } for p in powers
    ]), 200


@app.route('/powers/<int:id>')
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    return jsonify({
        "id": power.id,
        "name": power.name,
        "description": power.description
    }), 200


@app.route('/powers/<int:id>', methods=['PATCH'])
def patch_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    data = request.get_json()
    errors = []

    description = data.get('description')
    if description is not None:
        if not description.strip():
            errors.append("Description must be present.")
        elif len(description) < 20:
            errors.append("Description must be at least 20 characters long.")

    if errors:
        return jsonify({"errors": errors}), 422

    if description is not None:
        power.description = description

    db.session.add(power)
    db.session.commit()

    return jsonify({
        "id": power.id,
        "name": power.name,
        "description": power.description
    }), 200


@app.route('/hero_powers', methods=['POST'])
def post_hero_power():
    data = request.get_json()
    errors = []

    # Required fields
    try:
        strength = data['strength']
        hero_id = int(data['hero_id'])
        power_id = int(data['power_id'])
    except (KeyError, TypeError, ValueError):
        errors.append("Missing or invalid required fields (strength, hero_id, power_id).")

    # Strength validation
    if 'strength' in data and strength not in ['Strong', 'Weak', 'Average']:
        errors.append("Strength must be one of: 'Strong', 'Weak', 'Average'.")

    # Check existence of Hero and Power
    if 'hero_id' in data:
        hero = Hero.query.get(hero_id)
        if not hero:
            errors.append("Hero not found.")

    if 'power_id' in data:
        power = Power.query.get(power_id)
        if not power:
            errors.append("Power not found.")

    if errors:
        return jsonify({"errors": errors}), 422

    new_hp = HeroPower(
        strength=strength,
        hero_id=hero_id,
        power_id=power_id
    )

    db.session.add(new_hp)
    db.session.commit()

    return jsonify({
        "id": new_hp.id,
        "hero_id": new_hp.hero_id,
        "power_id": new_hp.power_id,
        "strength": new_hp.strength,
        "hero": {
            "id": new_hp.hero.id,
            "name": new_hp.hero.name,
            "super_name": new_hp.hero.super_name
        },
        "power": {
            "id": new_hp.power.id,
            "name": new_hp.power.name,
            "description": new_hp.power.description
        }
    }), 201


if __name__ == '__main__':
    app.run(port=5555, debug=True)