from flask import Blueprint, request, jsonify
from app.models import db, Hero, Power, HeroPower

main = Blueprint("main", __name__)

# GET /heroes
@main.route("/heroes", methods=["GET"])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes]), 200

# GET /heroes/<id>
@main.route("/heroes/<int:id>", methods=["GET"])
def get_hero(id):
    hero = Hero.query.get(id)
    if hero:
        return jsonify(hero.to_dict()), 200
    return jsonify({"error": "Hero not found"}), 404

# GET /powers
@main.route("/powers", methods=["GET"])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers]), 200

# GET /powers/<id>
@main.route("/powers/<int:id>", methods=["GET"])
def get_power(id):
    power = Power.query.get(id)
    if power:
        return jsonify(power.to_dict()), 200
    return jsonify({"error": "Power not found"}), 404

# PATCH /powers/<id>
@main.route("/powers/<int:id>", methods=["PATCH"])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    data = request.get_json()
    description = data.get("description")

    if not description or len(description) < 20:
        return jsonify({"errors": ["description must be at least 20 characters"]}), 400

    power.description = description
    db.session.commit()
    return jsonify(power.to_dict()), 200

# POST /hero_powers
@main.route("/hero_powers", methods=["POST"])
def create_hero_power():
    data = request.get_json()
    hero_id = data.get("hero_id")
    power_id = data.get("power_id")
    strength = data.get("strength")

    if strength not in ["Strong", "Average", "Weak"]:
        return jsonify({"errors": ["strength must be Strong, Average, or Weak"]}), 400

    hero = Hero.query.get(hero_id)
    power = Power.query.get(power_id)
    if not hero or not power:
        return jsonify({"errors": ["Invalid hero_id or power_id"]}), 400

    hero_power = HeroPower(hero_id=hero_id, power_id=power_id, strength=strength)
    db.session.add(hero_power)
    db.session.commit()
    return jsonify(hero_power.to_dict()), 201
