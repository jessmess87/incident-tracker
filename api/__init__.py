from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # ✅ Make sure this line is indented exactly once inside create_app()
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:login@localhost:5432/incident_api"





    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # register blueprints here
    from .users import bp as users_bp
    app.register_blueprint(users_bp)

    from .incidents import bp as incidents_bp
    app.register_blueprint(incidents_bp)

    from .comments import bp as comments_bp
    app.register_blueprint(comments_bp)

    from .categories import bp as categories_bp
    app.register_blueprint(categories_bp)

    return app
