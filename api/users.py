from flask import Blueprint, jsonify
from .models import User

bp = Blueprint("users", __name__, url_prefix="/users")

@bp.route("", methods=["GET"])
def index_users():
    return jsonify([u.serialize() for u in User.query.all()])


@bp.route("", methods=["POST"])
def create_user():
    data = request.get_json() or {}
    u = User(username=data["username"], email=data["email"], role=data.get("role", "reporter"))
    db.session.add(u)
    db.session.commit()
    return jsonify(u.serialize()), 201

@bp.route("/<int:id>", methods=["GET"])
def show_user(id):
    return jsonify(User.query.get_or_404(id).serialize())

@bp.route("/<int:id>", methods=["PUT", "PATCH"])
def update_user(id):
    u = User.query.get_or_404(id)
    data = request.get_json() or {}
    u.email = data.get("email", u.email)
    u.role = data.get("role", u.role)
    db.session.commit()
    return jsonify(u.serialize())

@bp.route("/<int:id>/incidents", methods=["GET"])
def user_incidents(id):
    u = User.query.get_or_404(id)
    reported = [i.serialize() for i in u.reported_incidents]
    assigned = [i.serialize() for i in u.assigned_incidents]
    return jsonify({"reported": reported, "assigned": assigned})
