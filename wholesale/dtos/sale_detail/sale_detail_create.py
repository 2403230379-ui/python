from pydantic import BaseModel

class SaleDetailCreateDTO(BaseModel):
    sale_id: int
    product_id: int
    quantity: int
