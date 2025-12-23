from flask import Blueprint, jsonify, request
from app import db
from app.models import Hero, Power, HeroPower

api = Blueprint('api', __name__)

# ---------------- HERO ROUTES ----------------
@api.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict(only=('id', 'name', 'super_name')) for hero in heroes]), 200


@api.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404

    return jsonify(hero.to_dict()), 200


# ---------------- POWER ROUTES ----------------
@api.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers]), 200


@api.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    return jsonify(power.to_dict()), 200


@api.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    try:
        data = request.get_json()
        power.description = data.get('description')
        db.session.commit()
        return jsonify(power.to_dict()), 200
    except Exception:
        db.session.rollback()
        return jsonify({"errors": ["validation errors"]}), 400


# ---------------- HERO POWER ROUTES ----------------
@api.route('/hero_powers', methods=['POST'])
def create_hero_power():
    try:
        data = request.get_json()
        hero_power = HeroPower(
            strength=data['strength'],
            hero_id=data['hero_id'],
            power_id=data['power_id']
        )
        db.session.add(hero_power)
        db.session.commit()
        return jsonify(hero_power.to_dict()), 201
    except Exception:
        db.session.rollback()
        return jsonify({"errors": ["validation errors"]}), 400
