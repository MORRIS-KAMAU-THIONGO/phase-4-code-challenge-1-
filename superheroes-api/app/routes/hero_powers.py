from flask import Blueprint, jsonify, request
from app.models import HeroPower
from app import db

bp = Blueprint("hero_powers", __name__)

@bp.route("/hero_powers", methods=["POST"])
def create_hero_power():
    data = request.get_json()

    try:
        hero_power = HeroPower(
            strength=data["strength"],
            hero_id=data["hero_id"],
            power_id=data["power_id"]
        )

        db.session.add(hero_power)
        db.session.commit()

        return jsonify(hero_power.to_dict()), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": [str(e)]}), 422
