from flask import Blueprint, jsonify
from app.models import Hero

bp = Blueprint("heroes", __name__)

@bp.route("/heroes", methods=["GET"])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes]), 200


@bp.route("/heroes/<int:id>", methods=["GET"])
def get_hero(id):
    hero = Hero.query.get(id)

    if not hero:
        return jsonify({"error": "Hero not found"}), 404

    return jsonify({
        "id": hero.id,
        "name": hero.name,
        "super_name": hero.super_name,
        "hero_powers": [
            {
                "id": hp.id,
                "hero_id": hp.hero_id,
                "power_id": hp.power_id,
                "strength": hp.strength,
                "power": hp.power.to_dict()
            }
            for hp in hero.hero_powers
        ]
    }), 200
