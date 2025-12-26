from flask import Blueprint, jsonify, request
from .models import Comment

bp = Blueprint("comments", __name__, url_prefix="/incidents")

@bp.route("/<int:incident_id>/comments", methods=["GET"])
def list_comments(incident_id):
    Incident.query.get_or_404(incident_id)  # ensure exists
    comments = Comment.query.filter_by(incident_id=incident_id).order_by(Comment.created_at.asc()).all()
    return jsonify([c.serialize() for c in comments])

@bp.route("/<int:incident_id>/comments", methods=["POST"])
def add_comment(incident_id):
    Incident.query.get_or_404(incident_id)
    data = request.get_json() or {}
    User.query.get_or_404(data["user_id"])
    c = Comment(incident_id=incident_id, user_id=data["user_id"], content=data["content"])
    db.session.add(c)
    db.session.commit()
    return jsonify(c.serialize()), 201
