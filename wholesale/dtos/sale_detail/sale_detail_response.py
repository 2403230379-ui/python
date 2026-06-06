from pydantic import BaseModel

class SaleDetailResponseDTO(BaseModel):
    id: int
    sale_id: int
    product_id: int
    quantity: int
    unit_price: float
    subtotal: float
