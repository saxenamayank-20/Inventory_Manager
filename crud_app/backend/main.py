from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from backend.database import engine, get_db
from backend import models, crud, schemas

# ─────────────────────────────────────────────
# Create all tables in MySQL on startup
# ─────────────────────────────────────────────
models.Base.metadata.create_all(bind=engine)

# ─────────────────────────────────────────────
# FastAPI App
# ─────────────────────────────────────────────
app = FastAPI(
    title="Item Inventory API",
    description="A full-stack CRUD API built with FastAPI and MySQL. Manage your inventory with ease!",
    version="1.0.0",
    contact={"name": "Mayank Saxena"},
)

# Allow Streamlit frontend to talk to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict this to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ─────────────────────────────────────────────
# Root
# ─────────────────────────────────────────────
@app.get("/", tags=["Health"])
def root():
    return {"message": "🚀 Item Inventory API is running!", "docs": "/docs"}


# ─────────────────────────────────────────────
# CREATE — POST /items
# ─────────────────────────────────────────────
@app.post(
    "/items",
    response_model=schemas.ItemResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Items"],
    summary="Create a new item",
)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    """Add a new item to the inventory database."""
    return crud.create_item(db=db, item=item)


# ─────────────────────────────────────────────
# READ ALL — GET /items
# ─────────────────────────────────────────────
@app.get(
    "/items",
    response_model=List[schemas.ItemResponse],
    tags=["Items"],
    summary="Get all items",
)
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Retrieve a paginated list of all items in the inventory."""
    return crud.get_items(db=db, skip=skip, limit=limit)


# ─────────────────────────────────────────────
# SEARCH — GET /items/search
# ─────────────────────────────────────────────
@app.get(
    "/items/search",
    response_model=List[schemas.ItemResponse],
    tags=["Items"],
    summary="Search items by name",
)
def search_items(keyword: str, db: Session = Depends(get_db)):
    """Search items by partial name match (case-insensitive)."""
    results = crud.search_items(db=db, keyword=keyword)
    if not results:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No items found matching '{keyword}'"
        )
    return results


# ─────────────────────────────────────────────
# READ ONE — GET /items/{item_id}
# ─────────────────────────────────────────────
@app.get(
    "/items/{item_id}",
    response_model=schemas.ItemResponse,
    tags=["Items"],
    summary="Get a single item by ID",
)
def read_item(item_id: int, db: Session = Depends(get_db)):
    """Retrieve a specific item from the database by its ID."""
    db_item = crud.get_item(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} not found"
        )
    return db_item


# ─────────────────────────────────────────────
# UPDATE — PUT /items/{item_id}
# ─────────────────────────────────────────────
@app.put(
    "/items/{item_id}",
    response_model=schemas.ItemResponse,
    tags=["Items"],
    summary="Update an existing item",
)
def update_item(item_id: int, updates: schemas.ItemUpdate, db: Session = Depends(get_db)):
    """Update one or more fields of an existing item. Only provided fields are updated."""
    updated = crud.update_item(db=db, item_id=item_id, updates=updates)
    if updated is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} not found"
        )
    return updated


# ─────────────────────────────────────────────
# DELETE — DELETE /items/{item_id}
# ─────────────────────────────────────────────
@app.delete(
    "/items/{item_id}",
    tags=["Items"],
    summary="Delete an item",
)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    """Permanently delete an item from the inventory by its ID."""
    deleted = crud.delete_item(db=db, item_id=item_id)
    if deleted is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} not found"
        )
    return {
        "message": f"✅ Item '{deleted.name}' (ID: {deleted.id}) deleted successfully."
    }
