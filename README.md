# Incident Tracking System

A full-featured Incident Tracking API designed to support creation, management, assignment, and commenting on incidents. Originally developed during Nucamp’s Python + SQL module and expanded during the DevOps module.

## 🚀 Features

- Create, update, and delete incidents  
- Assign incidents to users  
- Add comments  
- Track status and categories  
- Filter incidents by status, priority, or assignee  
- Includes ER diagrams and project documentation  

## 🗂 Project Structure
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

## 🧰 Tech Stack

- Python  
- Flask  
- SQL / PostgreSQL  
- SQLAlchemy  
- REST API design  

## 🛠 Setup Instructions

1. Create a virtual environment  
2. Install dependencies  
3. Run `setup_db.py` to initialize the database  
4. Start the API server  

## 📄 Documentation

Full project report and diagrams are available in the `/docs` folder.

## 📌 Future Enhancements

- Authentication  
- Audit logging  
- File attachments  
- Notification system  
- Docker containerization  
- CI/CD pipeline  
