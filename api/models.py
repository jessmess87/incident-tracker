from . import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # Relationships
    incidents_reported = db.relationship("Incident", foreign_keys="Incident.reporter_id", backref="reporter")
    incidents_assigned = db.relationship("Incident", foreign_keys="Incident.assignee_id", backref="assignee")

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }

class Incident(db.Model):
    __tablename__ = "incidents"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), nullable=False, default="open")
    severity = db.Column(db.String(20), nullable=False, default="medium")
    created_at = db.Column(db.DateTime)
    reporter_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    assignee_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "severity": self.severity
        }
class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime)

    # Foreign key to the incident this comment belongs to
    incident_id = db.Column(db.Integer, db.ForeignKey("incidents.id"), nullable=False)

    # Foreign key to the user who wrote the comment
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "created_at": self.created_at,
            "incident_id": self.incident_id,
            "user_id": self.user_id
        }
incident_categories = db.Table(
    "incident_categories",
    db.Column("incident_id", db.Integer, db.ForeignKey("incidents.id"), primary_key=True),
    db.Column("category_id", db.Integer, db.ForeignKey("categories.id"), primary_key=True)
)

class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    # Many-to-many relationship with incidents
    incidents = db.relationship(
        "Incident",
        secondary=incident_categories,
        backref="categories"
    )

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }
