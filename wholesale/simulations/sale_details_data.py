from dtos.sale_detail.sale_detail_response import SaleDetailResponseDTO

detail1 = SaleDetailResponseDTO(
    id=1,
    sale_id=1,
    product_id=1,
    quantity=2,
    unit_price=18.50,
    subtotal=37.00
)

sale_details_data = [detail1]
