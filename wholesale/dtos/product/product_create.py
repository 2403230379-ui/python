from pydantic import BaseModel, Field

class ProductCreateDTO(BaseModel):
    barcode: str = Field(min_length=1, max_length=50)
    name: str
    description: str
    brand: str
    price: float
    stock: int
