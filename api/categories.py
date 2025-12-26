from flask import Blueprint, jsonify, request
from .models import Category

bp = Blueprint("categories", __name__, url_prefix="/categories")

@bp.route("", methods=["GET"])
def index_categories():
    return jsonify([c.serialize() for c in Category.query.all()])

@bp.route("", methods=["POST"])
def create_category():
    data = request.get_json() or {}
    c = Category(name=data["name"], description=data.get("description"))
    db.session.add(c)
    db.session.commit()
    return jsonify(c.serialize()), 201

@bp.route("/<int:category_id>/incidents", methods=["GET"])
def incidents_by_category(category_id):
    from models import Category
    c = Category.query.get_or_404(category_id)
    return jsonify([i.serialize() for i in c.incidents])
