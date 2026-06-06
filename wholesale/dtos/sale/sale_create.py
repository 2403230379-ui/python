from pydantic import BaseModel

class SaleCreateDTO(BaseModel):
    location_id: int
