from pydantic import BaseModel

class SaleUpdateDTO(BaseModel):
    id: int
    status: str
