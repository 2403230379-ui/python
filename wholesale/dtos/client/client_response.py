from pydantic import BaseModel, EmailStr
from datetime import datetime

class ClientResponseDTO(BaseModel):
    id: int
    name: str
    phone: str
    email: EmailStr
    rfc: str
    active: bool
    created_at: datetime
    updated_at: datetime
