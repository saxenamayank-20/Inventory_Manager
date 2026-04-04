from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class ItemBase(BaseModel):
    """Shared fields used in both create and update schemas."""
    name:        str   = Field(..., min_length=1, max_length=100, example="Laptop")
    description: Optional[str] = Field(None, example="A powerful laptop")
    price:       float = Field(..., gt=0, example=49999.99)
    quantity:    int   = Field(..., ge=0, example=10)


class ItemCreate(ItemBase):
    """Schema for creating a new item (POST request body)."""
    pass


class ItemUpdate(BaseModel):
    """Schema for updating an existing item (PUT request body) — all fields optional."""
    name:        Optional[str]   = Field(None, min_length=1, max_length=100, example="Gaming Laptop")
    description: Optional[str]   = Field(None, example="Updated description")
    price:       Optional[float] = Field(None, gt=0, example=59999.99)
    quantity:    Optional[int]   = Field(None, ge=0, example=5)


class ItemResponse(ItemBase):
    """Schema for the API response that includes auto-generated fields."""
    id:         int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True  # Enables ORM model → Pydantic conversion
