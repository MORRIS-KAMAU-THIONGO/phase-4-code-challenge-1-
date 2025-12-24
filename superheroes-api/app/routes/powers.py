from flask import Blueprint, jsonify, request
from app.models import Power
from app import db

bp = Blueprint("powers", __name__)

@bp.route("/powers", methods=["GET"])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers]), 200


@bp.route("/powers/<int:id>", methods=["GET"])
def get_power(id):
    power = Power.query.get(id)

    if not power:
        return jsonify({"error": "Power not found"}), 404

    return jsonify(power.to_dict()), 200


@bp.route("/powers/<int:id>", methods=["PATCH"])
def update_power(id):
    power = Power.query.get(id)

    if not power:
        return jsonify({"error": "Power not found"}), 404

    try:
        data = request.get_json()
        power.description = data.get("description")
        db.session.commit()
        return jsonify(power.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": [str(e)]}), 422
