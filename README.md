# 📦 Item Inventory Manager — Full Stack App

A full-stack **CRUD** application built with:

| Layer      | Technology              |
|------------|-------------------------|
| Backend    | FastAPI + SQLAlchemy    |
| Frontend   | Streamlit               |
| Database   | MySQL                   |
| ORM        | SQLAlchemy              |
| Validation | Pydantic v2             |

---

## 🗂️ Project Structure

```
crud_app/
├── backend/
│   ├── __init__.py
│   ├── database.py     # SQLAlchemy engine & session
│   ├── models.py       # ORM models (Item table)
│   ├── schemas.py      # Pydantic request/response schemas
│   ├── crud.py         # CRUD database operations
│   └── main.py         # FastAPI routes & app
├── frontend/
│   └── app.py          # Streamlit frontend UI
├── .env                # DB credentials (update this!)
└── requirements.txt    # Python dependencies
```

---

## ⚙️ Prerequisites

1. **Python 3.10+** installed
2. **MySQL** installed and running
3. Create the database:
   ```sql
   CREATE DATABASE crud_db;
   ```

---

## 🚀 Setup & Run

### Step 1 — Install dependencies

```bash
cd crud_app
pip install -r requirements.txt
```

### Step 2 — Configure MySQL credentials

Edit the `.env` file:
```
DATABASE_URL=mysql+pymysql://root:YOUR_PASSWORD@localhost:3306/crud_db
```
Replace `YOUR_PASSWORD` with your MySQL root password.

### Step 3 — Start the FastAPI backend

Open a terminal and run from inside `crud_app/`:
```bash
uvicorn backend.main:app --reload
```

The API runs at: **http://127.0.0.1:8000**  
Swagger docs at: **http://127.0.0.1:8000/docs**

### Step 4 — Start the Streamlit frontend

Open **another terminal** and run from inside `crud_app/`:
```bash
streamlit run frontend/app.py
```

The UI opens at: **http://localhost:8501**

---

## 📡 API Endpoints

| Method   | Endpoint              | Description              |
|----------|-----------------------|--------------------------|
| `GET`    | `/`                   | Health check             |
| `POST`   | `/items`              | Create a new item        |
| `GET`    | `/items`              | List all items           |
| `GET`    | `/items/{id}`         | Get item by ID           |
| `GET`    | `/items/search?keyword=` | Search items by name |
| `PUT`    | `/items/{id}`         | Update item by ID        |
| `DELETE` | `/items/{id}`         | Delete item by ID        |

---

## 🖥️ Frontend Pages

| Page            | Feature                          |
|-----------------|----------------------------------|
| 🏠 Dashboard    | KPI metrics + full items table   |
| ➕ Add Item     | Form to create a new item        |
| ✏️ Update Item  | Load item by ID and edit fields  |
| 🗑️ Delete Item | Preview + confirm delete by ID   |
| 🔍 Search       | Search items by name keyword     |

⭐ **Star this repo** if you find it helpful!