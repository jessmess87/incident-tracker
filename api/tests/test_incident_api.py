import pytest

def test_create_incident(client):
    payload = {
        "title": "Server outage",
        "description": "Production server is down",
        "priority": "High",
        "status": "Open",
        "assignee_id": 1,
        "reporter_id": 1
    }

    response = client.post("/incidents", json=payload)

    assert response.status_code == 201
    data = response.get_json()

    assert data["title"] == payload["title"]
    assert "id" in data


def test_get_incidents(client):
    # Create an incident so the list isn't empty
    payload = {
        "title": "Server outage",
        "description": "Production server is down",
        "reporter_id": 1,
        "assignee_id": 1
    }
    client.post("/incidents", json=payload)

    # Now fetch the list
    response = client.get("/incidents")

    assert response.status_code == 200
    data = response.get_json()

    assert isinstance(data, list)
    assert len(data) >= 1


def test_get_single_incident(client):
    # First create an incident
    payload = {
        "title": "VPN issue",
        "description": "Users cannot connect to VPN",
        "reporter_id": 1,
        "assignee_id": 1
    }
    create_res = client.post("/incidents", json=payload)
    created = create_res.get_json()
    incident_id = created["id"]

    # Now fetch it
    response = client.get(f"/incidents/{incident_id}")

    assert response.status_code == 200
    data = response.get_json()

    assert data["id"] == incident_id
    assert data["title"] == "VPN issue"

def test_update_incident(client):
    # Create an incident
    payload = {
        "title": "Old title",
        "description": "Old description",
        "reporter_id": 1,
        "assignee_id": 1
    }
    create_res = client.post("/incidents", json=payload)
    created = create_res.get_json()
    incident_id = created["id"]

    # Update the incident
    update_payload = {
        "title": "Updated title",
        "description": "Updated description"
    }
    response = client.put(f"/incidents/{incident_id}", json=update_payload)

    assert response.status_code == 200
    data = response.get_json()

    assert data["title"] == "Updated title"
    assert data["description"] == "Updated description"

def test_delete_incident(client):
    # Create an incident
    payload = {
        "title": "Delete me",
        "description": "To be removed",
        "reporter_id": 1,
        "assignee_id": 1
    }
    create_res = client.post("/incidents", json=payload)
    incident_id = create_res.get_json()["id"]

    # Delete the incident
    response = client.delete(f"/incidents/{incident_id}")
    assert response.status_code == 200

    # Confirm it's gone
    get_res = client.get(f"/incidents/{incident_id}")
    assert get_res.status_code == 404
