from datetime import datetime, timezone
from dtos.location.location_response import LocationResponseDTO

now = datetime.now(timezone.utc)

location1 = LocationResponseDTO(
    id=1,
    client_id=1,
    name="Sucursal Centro",
    address="Av. Revolucion 123",
    city="Tijuana",
    state="Baja California",
    postal_code="22000",
    phone="6641112233",
    email="centro@email.com",
    active=True,
    created_at=now,
    updated_at=now
)

location2 = LocationResponseDTO(
    id=2,
    client_id=2,
    name="Sucursal Norte",
    address="Blvd. Agua Caliente 456",
    city="Tijuana",
    state="Baja California",
    postal_code="22010",
    phone="6644445566",
    email="norte@email.com",
    active=True,
    created_at=now,
    updated_at=now
)

locations_data = [location1, location2]
