from pydantic import BaseModel
from datetime import datetime

class ProductResponseDTO(BaseModel):
    id: int
    barcode: str
    name: str
    description: str
    brand: str
    price: float
    stock: int
    active: bool
    created_at: datetime
    updated_at: datetime
