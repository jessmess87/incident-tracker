import pytest
from api import create_app, db
from api.models import User

@pytest.fixture
def client():
    app = create_app(testing=True)

    with app.app_context():
        db.create_all()

        # Create a dummy user so reporter_id=1 and assignee_id=1 are valid
        user = User(username="tester", email="tester@example.com")
        db.session.add(user)
        db.session.commit()

        yield app.test_client()

        db.drop_all()
