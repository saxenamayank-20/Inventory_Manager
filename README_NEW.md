# Inventory Manager

## 🔍 Description
A comprehensive full-stack inventory management system that allows users to efficiently manage, track, and organize inventory items. This application provides real-time CRUD operations with a user-friendly interface and robust backend API for seamless data management and reporting.

## ⚙️ Tech Stack
- **Python** - Core programming language
- **FastAPI** - Modern web framework for building APIs
- **SQLAlchemy** - ORM for database operations
- **MySQL/SQL** - Relational database
- **Streamlit** - Interactive frontend UI
- **Pydantic** - Data validation

## 🚀 Features
- **Login System** - Secure user authentication and authorization
- **Dashboard** - Real-time inventory overview with metrics and analytics
- **API Integration** - RESTful API endpoints for all CRUD operations
- **Search & Filter** - Advanced search functionality by item name and properties
- **Inventory Tracking** - Monitor stock levels and item details
- **Add/Edit/Delete Items** - Complete CRUD operations for inventory management
- **Data Validation** - Ensure data integrity with Pydantic models
- **API Documentation** - Interactive Swagger UI for API exploration

## 📸 Screenshots
<!-- Add screenshots here -->
- Dashboard view
- Add item form
- Inventory list
- Search results

## 🧠 Learnings
- Building scalable full-stack applications with separation of concerns
- Implementing RESTful API design patterns
- Working with SQLAlchemy ORM for efficient database operations
- Creating responsive web interfaces with Streamlit
- Database schema design for inventory management
- Request/response validation with Pydantic v2
- Authentication and authorization implementation
- API documentation and Swagger integration

## ▶️ How to Run

### Prerequisites
1. **Python 3.10+** installed on your system
2. **MySQL** installed and running
3. Create the database:
   ```sql
   CREATE DATABASE crud_db;
   ```

### Steps to Run

**Step 1** — Clone the repository and navigate to the project directory
```bash
cd Inventory_Manager
```

**Step 2** — Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

**Step 3** — Install dependencies
```bash
pip install -r requirements.txt
```

**Step 4** — Configure database credentials
Edit the `.env` file:
```
DATABASE_URL=mysql+pymysql://root:YOUR_PASSWORD@localhost:3306/crud_db
```

**Step 5** — Start the FastAPI backend (Terminal 1)
```bash
uvicorn backend.main:app --reload
```
Backend API: http://127.0.0.1:8000  
API Docs: http://127.0.0.1:8000/docs

**Step 6** — Start the Streamlit frontend (Terminal 2)
```bash
streamlit run frontend/app.py
```
Frontend: http://localhost:8501

---

## 📊 API Endpoints Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Health check |
| POST | /items | Create new item |
| GET | /items | List all items |
| GET | /items/{id} | Get item by ID |
| PUT | /items/{id} | Update item |
| DELETE | /items/{id} | Delete item |
| GET | /items/search | Search items |

---

**⭐ If you found this helpful, consider starring the repository!**
