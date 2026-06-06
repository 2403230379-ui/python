from pydantic import BaseModel
from datetime import datetime

class SaleResponseDTO(BaseModel):
    id: int
    folio: str
    location_id: int
    datetime: datetime
    total: float
    status: str
    created_at: datetime
    updated_at: datetime
