from pydantic import BaseModel, EmailStr
from datetime import datetime

class LocationResponseDTO(BaseModel):
    id: int
    client_id: int
    name: str
    address: str
    city: str
    state: str
    postal_code: str
    phone: str
    email: EmailStr
    active: bool
    created_at: datetime
    updated_at: datetime
