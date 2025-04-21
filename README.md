## Todo List Application - README
## 1. Overview
This is a simple **Todo List Application** built using the **Flask** web framework. The application allows users to manage their tasks (create, update, delete, and toggle completion status) through both a web interface and a RESTful API.

### Video Clip : https://youtu.be/PbS4loPp1Is

---
## 2. Environments of the Software Development and Running

### 2.1 Programming Language
- **Python 3.x**

### 2.2 Minimum Hardware Requirements
- CPU: Dual-core processor or higher.
- RAM: At least 2GB (4GB recommended for better performance).
- Storage: At least 500MB free space.

### 2.3 Software Requirements
- **Operating System**: Windows, macOS, or Linux.
- **Database**: MySQL Server (tested with MySQL 8.0).
- **Python Packages**:
  - Flask (`pip install flask`)
  - Flask-SQLAlchemy (`pip install flask-sqlalchemy`)
  - PyMySQL (`pip install pymysql`)

### 2.4 Required Packages
Install the required Python packages using the following command:
```bash
pip install flask flask-sqlalchemy pymysql
```
---
## 3. Environment Setup
1. Install MySQL and create a user with appropriate privileges.
2. Update the `init_db()` function in the code with your MySQL credentials (`host`, `user`, `password`).
3. Run the application script to initialize the database and start the server:
   ```bash
   python app.py
   ```
4. Access the web interface at http://localhost:5001/.

---

## 4. Technical Components --- Declaration

###  4.1 Open Source Libraries Used
- **Flask**: A lightweight web framework for Python. [License: BSD](https://flask.palletsprojects.com/)
- **Flask-SQLAlchemy**: An extension for Flask that adds support for SQLAlchemy. [License: BSD](https://flask-sqlalchemy.palletsprojects.com/)
- **PyMySQL**: A pure-Python MySQL client library. [License: MIT](https://pymysql.readthedocs.io/)

### 4.2 Third-Party Resources
No third-party resources outside of the Python ecosystem were used in this project.

### 4.3 Custom Code
All other parts of the application, including the logic for handling HTTP requests, interacting with the database, and rendering templates, were developed independently.

---
##  5. Algorithm
The application uses basic CRUD (Create, Read, Update, Delete) operations to manage the tasks stored in a MySQL database. The following algorithms are implemented:
1. **Task Creation**: Add new tasks with a title and default status (`completed=False`).
2. **Task Retrieval**: Fetch all tasks from the database, sorted by creation time in descending order.
3. **Task Update**: Modify task attributes such as title or completion status.
4. **Task Deletion**: Remove tasks permanently from the database.
5. **Task Toggle**: Switch the completion status (`completed`) of a task between `True` and `False`.

---

##  6. Current Status (Week 5)
- **Status**: Fully functional and tested.
- **Features**:
  - Web Interface: Users can interact with the app via HTML forms.
  - RESTful API: Developers can programmatically interact with the app using JSON-based API endpoints.
  - Database Integration: Tasks are stored in a MySQL database for persistence.
-   **Key Functions**:
     -  1. Create a Task
At the top of the page, there's an input form where users can enter the title of a new task. Once submitted, the task is added to the list with a default status of incomplete.
      - 2. Toggle Task Completion
Each task is accompanied by a checkbox. Users can click to mark a task as complete or revert it to incomplete.
This interaction is handled instantly using AJAX, without requiring a page reload.
    - 3. Delete a Task
Every task entry has a “Delete” button. Clicking it removes the task both from the page and from the database in real time.
This responsive interface is enhanced with Bootstrap 5, ensuring compatibility across different screen sizes and devices
- **Known Issues**: None at the moment.
---
##  7. Usage Instructions

###  7.1 Web Interface
1. Navigate to `http://localhost:5001/` in your browser.
2. Use the form to add new tasks.
3. Click on a task's checkbox to toggle its completion status.
4. Use the "Delete" button to remove tasks.

###  7.2 RESTful API Endpoints
#### 1. Get All Tasks
- **URL**: `/api/todos`
- **Method**: `GET`
- **Response**: JSON array of tasks.

#### 2. Create a New Task
- **URL**: `/api/todos`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "title": "Task Title"
  }
  ```
- **Response**: JSON object representing the newly created task.

#### 3. Update a Task
- **URL**: `/api/todos/<todo_id>`
- **Method**: `PUT`
- **Request Body**:
  ```json
  {
    "title": "Updated Title",
    "completed": true
  }
  ```
- **Response**: JSON object representing the updated task.

#### 4. Delete a Task
- **URL**: `/api/todos/<todo_id>`
- **Method**: `DELETE`
- **Response**: Empty response with status code `204`.

---
##  8. Future Improvements
1. **Add user authentication** to allow multiple users to manage their own tasks.
2. Implement **pagination** for the API to handle large datasets efficiently.
3. Enhance the UI with modern frontend frameworks like **React or Vue.js**.
4. **Add unit tests** for better reliability and maintainability.

---
## 9. Team Responsibilities (Week 5)
The following table represents the specific division of labor for our team to complete this project within five weeks：

| Member (ID)       | Role                  | Key Contributions Completed                                                                 |
|--------------------|-----------------------|---------------------------------------------------------------------------------------------|
|   Yu (P2320402)      | Project & Documentation | – Defined bi-weekly iteration plans and led sprint meetings<br>– Authored API documentation and user manual<br>– Coordinated front-end/back-end OpenAPI 3.0 interface specifications |
| HAO KENG KEI （P2304547）      | Back-End Development  | – Implemented core RESTful API logic (CRUD operations)<br>– Designed database access layer (SQLAlchemy models)<br>– Developed task-status toggle algorithm (boolean logic conversion) |
| Harry (P2320168)   | Front-End Development | – Built Jinja2 template system (task list rendering)<br>– Implemented AJAX asynchronous operations (delete button interactions)<br>– Developed responsive layout (Bootstrap 5) |
| Lin (P2320443)     | Database              | – Designed MySQL database schema (including index optimization)<br>– Implemented database migration script (`init_db()` function)<br>– Configured query performance monitoring (slow-query log analysis) |
| Alex (P2320265)    | DevOps & Testing      | – Set up GitHub Actions CI pipeline<br>– Wrote pytest test suite (covering 90% of API endpoints)<br>– Configured Docker development environment (MySQL + Flask containerization) |
---
# 10. Twelve-Week Development Plan

## Overview

- **Duration**: 12 weeks (6 two-week sprints; Sprints 1-2.5 completed, Sprints 3-6 remaining)  
- **Methodology**: Agile (Scrum), each sprint includes planning, development, review, and retrospective  
- **Goal**: Evolve from MVP to full production-grade application, covering user authentication, performance optimization, and modern front-end  

---

## 10.1 Completed Phases (Weeks 0-5)

| Sprint    | Time         | Deliverables                                                                 | Team Members       |
|-----------|--------------|------------------------------------------------------------------------------|--------------------|
| **Sprint 1** | Weeks 0–2    | – Requirements analysis & prototype design<br>– Finalized MySQL schema<br>– Core CRUD API implementation | Yu, HAO, Lin       |
| **Sprint 2** | Weeks 3–4    | – Web interface development (Jinja2 templates)<br>– Automated testing framework setup<br>– CI/CD pipeline configuration | Harry, Alex        |
| **Sprint 2.5** | Week 5     | – API performance benchmarking<br>– Initial documentation draft             | Yu, Alex           |

---

## 10.2 Future Phases (Weeks 6-12)

### **Sprint 3 (Weeks 6–7): Build user authentication system**  
- **Objective**: Support multi-user isolated task management  
- **Deliverables**:  
  – JWT auth API (`/auth/login`, `/auth/register`)  
  – User role model (Admin/User)  
  – Front-end login/register pages (React components)  


### **Sprint 4 (Weeks 8–9): Optimize API Performance & Add Pagination**  
- **Objective**:  
  Improve API scalability and response efficiency for large datasets.  

- **Key Deliverables**:  
   1. **Pagination API**  
     – Implement `GET /api/todos?page=<num>&size=<items>` endpoint  
     – Design cursor-based pagination for real-time data consistency  
     – Integrate pagination metadata in responses:  
    ```json
    {
      "tasks": [ ... ],
      "pagination": {
        "total": 1500,
        "page": 2,
        "size": 50
      }
    }
    ```  

  2. **Performance Optimization**  
  – Reduce API latency by 40% through:  
   – MySQL query optimization (index tuning via `EXPLAIN ANALYZE`)  
   – Connection pooling with `SQLAlchemy QueuePool`  
 – Conduct load testing using Locust (simulate 5,000 concurrent users)  

  3. **Developer Tooling**  
 – Add Prometheus metrics endpoint for API monitoring  
  – Generate Swagger docs with pagination parameters  

---

### **Sprint 5 (Weeks 10–11): Implement Caching Mechanism & Load Balancing**  
- **Objective**:  
  Achieve sub-100ms response times under high traffic.  

- **Key Deliverables**:  
  1. **Redis Caching Layer**  
  – Cache frequent queries (e.g., `GET /api/todos`) with 15-minute TTL  
  – Implement cache invalidation on write operations (`POST/PUT/DELETE`)  
  – Configuration:  
    ```python
    redis_client = Redis(host='redis', port=6379, decode_responses=True)
    ```  

  2. **Horizontal Scaling**  
  – Dockerize app with `docker-compose.prod.yml` for:  
   – Flask app (3 replicas)  
   – MySQL cluster (1 primary + 2 replicas)  
   – Redis Sentinel  
  – Configure NGINX as load balancer with least_conn algorithm  

  3. **Disaster Recovery**  
  –  Implement automated database backups to AWS S3  
  – Design failover playbook for Redis/Master-Slave switches  


---

### **Sprint 6 (Week 12): Final Testing & Production Deployment**  
- **Objective**:  
  Ensure production readiness and zero-downtime deployment.  

- **Key Deliverables**:  
  1. **Comprehensive Testing**  
 – **Security**: OWASP ZAP penetration testing  
  – **Performance**: Validate 10k RPM capacity  
  – **User Acceptance**: Conduct beta testing with 50 external users  

  2. **Blue-Green Deployment**  
  – Setup using AWS ECS:  
    ```terraform
    resource "aws_ecs_service" "blue" {
      deployment_controller {
        type = "BLUE_GREEN"
      }
    }
    ```  
        Implement health checks and automatic rollback on failure  

  **Observability Suite**  
– Centralized logging via ELK Stack  
  – Grafana dashboard for real-time metrics:  
  – API success rate (>99.95%)  
– Cache hit ratio (>80%)  
 – DB replication lag (<200ms)  

## 11. Purpose of the software 

### Why Agile (vs. Waterfall)

### 1. Precise Response to Evolving Requirements  
In a tool-type application like a Todo List, users often request new interaction features (e.g., task tags, file attachments). Through bi-weekly sprints, we achieved:  

- **Sprint 1**: Rapid delivery of core CRUD functionality to validate feasibility  
- **Sprint 3**: Addition of task-priority feature (Urgent/Important) based on user feedback  
- Dynamic task ordering via Trello board to prioritize high-value requirements  

**Example**:  
While developing the RESTful API, JSON support was the original plan. Based on community feedback, CSV export functionality was added within 24 hours during Sprint 

### 2. Early Exposure of Technical Risks  
**Protective Mechanism**: For critical risk points such as database operations and API concurrency, agile practice provides early feedback loops. For example, after Sprint 1, daily automated builds run on every commit via GitHub Actions:  
-``` name: Run Pytest|
     run: |
    |pytest tests/ --cov=app --cov-report=xml```
 
### 3. Efficient Cross-Functional Team Collaboration  
**Collaboration Model**: For front-end/back-end separation, the agile toolchain is key. For example, front-end (Harry) and back-end (HAO) worked in parallel using the OpenAPI spec, reducing idle time.

---
### **Possible Usage & Target Market:**

-   **Individual Users:** Students and freelancers who need a lightweight web app to manage their daily to‑do items.
    
-   **Small Team Collaboration:** Project teams that require shared task lists and asynchronous status updates.
    
-   **Educational & Prototyping:** As a Flask‑based tutorial example or early prototype for teaching, research, hackathons, and similar scenarios.
---

## 12. License
This project is licensed under the **MIT License**. Feel free to use, modify, and distribute it as needed.

---
## 13. Contact
For questions or feedback, please contact the developer:
- Email: p2320265@mpu.edu.mo
