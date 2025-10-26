from pydantic import BaseModel, Field
from typing import Optional


class CartItemBase(BaseModel):
    product_id: int = Field(..., description="Product of identifier")
    quantity: int = Field(
        ..., gt=0, description="Quantity of the product (must be greater than 0)"
    )


class CartItemCreate(CartItemBase):
    pass


class CartItemUpdate(BaseModel):
    product_id: int = Field(..., description="Product of identifier")
    quantity: int = Field(
        ..., gt=0, description="New quantity of the product (must be greater than 0)"
    )


class CartItem(BaseModel):
    product_id: int
    name: str = Field(..., description="Product name")
    price: float = Field(..., description="Product price")
    quantity: int = Field(..., gt=0, description="Quantity in cart")
    subtotal: float = Field(..., description="Total for this item (price * quantity)")
    image_url: Optional[str] = Field(None, description="Product image URL")


class CartResponse(BaseModel):
    items: list[CartItem] = Field(..., description="List of items in the cart")
    items_count: int = Field(..., description="Total number of items in the cart")
    total: float = Field(..., description="Total cart price")
