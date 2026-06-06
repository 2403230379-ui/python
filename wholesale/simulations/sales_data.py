from datetime import datetime, timezone
from dtos.sale.sale_response import SaleResponseDTO

now = datetime.now(timezone.utc)

sale1 = SaleResponseDTO(
    id=1,
    folio="VTA-0001",
    location_id=1,
    datetime=now,
    total=37.00,
    status="open",
    created_at=now,
    updated_at=now
)

sales_data = [sale1]
