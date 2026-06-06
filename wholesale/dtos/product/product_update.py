from pydantic import BaseModel, Field

class ProductUpdateDTO(BaseModel):
    id: int
    barcode: str = Field(min_length=1, max_length=50)
    name: str
    description: str
    brand: str
    price: float
    stock: int
