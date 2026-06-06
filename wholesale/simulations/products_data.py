from datetime import datetime, timezone
from dtos.product.product_response import ProductResponseDTO

now = datetime.now(timezone.utc)

product1 = ProductResponseDTO(
    id=1,
    barcode="7501000000001",
    name="Refresco Cola 600ml",
    description="Refresco sabor cola botella 600ml",
    brand="CocaCola",
    price=18.50,
    stock=100,
    active=True,
    created_at=now,
    updated_at=now
)

product2 = ProductResponseDTO(
    id=2,
    barcode="7501000000002",
    name="Agua Natural 1L",
    description="Agua purificada botella 1 litro",
    brand="Bonafont",
    price=12.00,
    stock=200,
    active=True,
    created_at=now,
    updated_at=now
)

product3 = ProductResponseDTO(
    id=3,
    barcode="7501000000003",
    name="Papas Fritas 45g",
    description="Papas fritas sabor original",
    brand="Sabritas",
    price=15.00,
    stock=150,
    active=True,
    created_at=now,
    updated_at=now
)

products_data = [product1, product2, product3]
