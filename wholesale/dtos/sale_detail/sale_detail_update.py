from pydantic import BaseModel

class SaleDetailUpdateDTO(BaseModel):
    id: int
    quantity: int
