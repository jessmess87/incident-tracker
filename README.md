<h1><span style="color:#4A90E2">📘 Incident Tracking System</span></h1>

<span style="color:#555">
A full-featured Incident Tracking API designed to support creation, management, assignment, and commenting on incidents. Originally developed during Nucamp’s Python + SQL module and expanded during the DevOps module.
</span>

---

<h2><span style="color:#E67E22">🚀 Features</span></h2>

- <span style="color:#2ecc71">Create, update, and delete incidents</span>  
- <span style="color:#2ecc71">Assign incidents to users</span>  
- <span style="color:#2ecc71">Add comments</span>  
- <span style="color:#2ecc71">Track status and categories</span>  
- <span style="color:#2ecc71">Filter incidents by status, priority, or assignee</span>  
- <span style="color:#2ecc71">Includes ER diagrams and project documentation</span>  

---

<h2><span style="color:#9B59B6">🗂 Project Structure</span></h2>



## Project Structure

Incident Tracker/
│
├── api/                     # Full API source code
│   ├── categories.py
│   ├── comments.py
│   ├── incidents.py
│   ├── models.py
│   ├── setup_db.py
│   ├── users.py
│   └── README.md
│
├── docs/                    # Documentation and diagrams
│   ├── Portfolio_Project_Report_Jessica_Long.pdf
│   ├── diagram.png
│   └── status.png
│
├── .gitignore
└── README.md


---

## Tech Stack

- Python  
- Flask  
- SQL / PostgreSQL  
- SQLAlchemy  
- REST API design  

---

---

<h2><span style="color:#16A085">🧰 Tech Stack</span></h2>

- Python  
- Flask  
- SQL / PostgreSQL  
- SQLAlchemy  
- REST API design  

---

<h2><span style="color:#D35400">🛠 Setup Instructions</span></h2>

1. Create a virtual environment  
2. Install dependencies  
3. Run `setup_db.py` to initialize the database  
4. Start the API server  

---

<h2><span style="color:#2980B9">📄 Documentation</span></h2>

Full project report and diagrams are available in the `/docs` folder.

---

<h1><span style="color:#C0392B">🧪 Testing</span></h1>

<span style="color:#555">
This project includes an automated test suite built with <strong>pytest</strong> to validate the core functionality of the Incident Tracking API. Tests run against an in-memory SQLite database, ensuring they are fast, isolated, and do not affect the production PostgreSQL environment.
</span>

---

<h3><span style="color:#27AE60">Running Tests</span></h3>

```bash
python -m pytest -v


<h3><span style="color:#8E44AD">How the Test Environment Works</span></h3>

The test suite uses a conftest.py fixture that:

Creates a fresh Flask application using create_app(testing=True)

Switches the database to sqlite:///:memory: for fast, isolated tests

Calls db.create_all() to build a clean schema for each test session

Seeds a dummy user so reporter_id and assignee_id foreign keys are valid

Provides a Flask test client for making API requests


<h3><span style="color:#E74C3C">Tests Included</span></h3>
Test Name	Description

test_create_incident	Ensures POST /incidents creates a new incident and returns 201
test_get_incidents	Ensures GET /incidents returns a list of incidents
test_get_single_incident	Ensures GET /incidents/ returns the correct incident
test_update_incident	Ensures PUT /incidents/ updates an existing incident
test_delete_incident	Ensures DELETE /incidents/ removes an incident and returns 404 on subsequent fetch

<h2><span style="color:#F39C12">📌 Future Enhancements</span></h2>
Authentication
Audit logging
File attachments
Notification system
Docker containerization
CI/CD pipeline