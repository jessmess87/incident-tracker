from flask import Blueprint, jsonify, request
from .models import Incident

bp = Blueprint("incidents", __name__, url_prefix="/incidents")

@bp.route("", methods=["GET"])
def index_incidents():
    q = Incident.query
    status = request.args.get("status")
    severity = request.args.get("severity")
    assignee_id = request.args.get("assignee_id")

    if status: q = q.filter(Incident.status == status)
    if severity: q = q.filter(Incident.severity == severity)
    if assignee_id: q = q.filter(Incident.assignee_id == int(assignee_id))

    return jsonify([i.serialize() for i in q.all()])

@bp.route("", methods=["POST"])
def create_incident():
    data = request.get_json() or {}
    i = Incident(
        title=data["title"],
        description=data["description"],
        status=data.get("status", "open"),
        severity=data.get("severity", "medium"),
        reporter_id=data["reporter_id"],
        assignee_id=data.get("assignee_id")
    )
    # Attach categories if provided
    category_ids = data.get("category_ids", [])
    if category_ids:
        i.categories = Category.query.filter(Category.id.in_(category_ids)).all()

    db.session.add(i)
    db.session.commit()
    return jsonify(i.serialize()), 201

@bp.route("/<int:id>", methods=["GET"])
def show_incident(id):
    return jsonify(Incident.query.get_or_404(id).serialize())

@bp.route("/<int:id>", methods=["PUT", "PATCH"])
def update_incident(id):
    i = Incident.query.get_or_404(id)
    data = request.get_json() or {}
    i.title = data.get("title", i.title)
    i.description = data.get("description", i.description)
    i.status = data.get("status", i.status)
    i.severity = data.get("severity", i.severity)
    i.assignee_id = data.get("assignee_id", i.assignee_id)

    # Update categories
    if "category_ids" in data:
        i.categories = Category.query.filter(Category.id.in_(data["category_ids"])).all()

    db.session.commit()
    return jsonify(i.serialize())

@bp.route("/<int:id>", methods=["DELETE"])
def delete_incident(id):
    i = Incident.query.get_or_404(id)
    db.session.delete(i)
    db.session.commit()
    return jsonify({"deleted": id})
