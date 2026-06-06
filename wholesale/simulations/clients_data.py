from datetime import datetime, timezone
from dtos.client.client_response import ClientResponseDTO

now = datetime.now(timezone.utc)

client1 = ClientResponseDTO(
    id=1,
    name="Juan Perez",
    phone="6641234567",
    email="juan@email.com",
    rfc="PEJJ900101AB1",
    active=True,
    created_at=now,
    updated_at=now
)

client2 = ClientResponseDTO(
    id=2,
    name="Maria Lopez",
    phone="6649876543",
    email="maria@email.com",
    rfc="LOMA850215CD2",
    active=True,
    created_at=now,
    updated_at=now
)

clients_data = [client1, client2]
