from incident_api import create_app, db

app = create_app()

with app.app_context():
    print("Connected to:", db.engine.url)
    db.create_all()
    print("✅ All tables created successfully.")



