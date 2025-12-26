# Portfolio Project: Incidents Tracking API

## 📖 Description
This project implements an Incidents Tracking API using Flask, SQLAlchemy, and PostgreSQL.  
It allows users to report incidents, assign them to other users, categorize them, and add comments.  
The project demonstrates RESTful design, relational database modeling, and error handling.

---

## 🔗 API Reference

| Endpoint                                | Method(s)   | Description                                      |
|-----------------------------------------|-------------|--------------------------------------------------|
| `/users`                                | GET, POST   | List all users / Create a new user               |
| `/users/<id>`                           | GET, PUT/PATCH, DELETE | Show, update, or delete a user        |
| `/users/<id>/incidents`                 | GET         | List incidents reported or assigned to a user    |
| `/incidents`                            | GET, POST   | List all incidents / Create a new incident       |
| `/incidents/<id>`                       | GET, PUT/PATCH, DELETE | Show, update, or delete an incident |
| `/incidents/<id>/comments`              | GET, POST   | List or add comments to an incident              |
| `/categories`                           | GET, POST   | List all categories / Create a new category      |
| `/categories/<id>/incidents`            | GET         | List incidents belonging to a category           |

---

## ⚡ Performance Improvements
- Added indexes on `status`, `severity`, `reporter_id`, and `assignee_id` to speed up queries.  
- Simplified queries with filters (`?status=open&severity=high`) to reduce load.  
- Validated correctness, speed, and memory usage across endpoints.

---

## 🔍 Retrospective

### Question 1: How did the project’s design evolve over time?
The design started with basic CRUD for users and incidents, then expanded to include categories and comments.  
Backrefs and many‑to‑many relationships were added to support flexible classification and richer queries.

### Question 2: Did you choose to use an ORM or raw SQL? Why?
I chose SQLAlchemy ORM because it integrates smoothly with Flask and makes relationships easier to manage.  
It reduced boilerplate and allowed me to focus on API design rather than raw SQL queries.

### Question 3: Potential Future Endpoints
- **Follow System for users**: `POST /users/<id>/follow`, `GET /users/<id>/followers`  
- **Incident lifecycle**: `POST /incidents/<id>/resolve`, `GET /incidents/<id>/history`  
- **Search**: `GET /incidents/search?query=<keyword>`  
- **Analytics**: `GET /incidents/stats` for severity distribution, MTTR, and workload per user  

These would make the app more realistic for real‑world incident management.

### Question 4: Challenges and Learnings
- **Challenges**:  
  - Blueprint registration issues (routes not showing until properly registered).  
  - Environment setup errors (using `python -m flask` instead of `flask` directly).  
  - Silent crashes in Insomnia when imports or logic were missing.  
  - 404 errors when testing endpoints with IDs that didn’t exist.  

- **Learnings**:  
  - How to use `flask routes` to validate endpoints.  
  - The importance of restarting Flask after code changes.  
  - How backrefs and many‑to‑many tables simplify relationship endpoints.  
  - The value of error handling and logging for debugging API behavior.  

---

## 🚀 Future Improvements
- Implement role‑based access (reporters vs. assignees vs. admins).  
- Add notifications when incidents are assigned or resolved.  
- Build visualization dashboards for incident trends and severity distribution.  
- Add authentication and authorization for secure access.  

## 🗄️ Database Schema
- **users**: id, username, email
- **incidents**: id, title, description, status, reporter_id, assignee_id
- **comments**: id, incident_id, content
- **categories**: id, name
- **incident_categories**: incident_id, category_id

![ER Diagram](diagram.png)
### Example Index
```sql
CREATE INDEX idx_incident_status ON incidents(status);

### 📊 Data Visualization

### Incidents by Status Chart (status.png)
![Incidents by Status](status.png)

```python
query = "SELECT status, COUNT(*) FROM incidents GROUP BY status;"
df = pd.read_sql(query, con)
df.plot(kind="bar", x="status", y="count", legend=False)
plt.title("Incidents by Status")
plt.show()



## ✅ Submission Contents
- PostgreSQL schema + ER diagram
- Flask REST API with CRUD endpoints
- Insomnia request collection
- Performance improvements (indexes + query analysis)
- README.md with documentation and retrospective
- *(Optional)* Data visualizations
# incidents-tracking-api
