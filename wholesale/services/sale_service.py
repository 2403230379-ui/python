from fastapi import HTTPException
from starlette import status
from datetime import datetime, timezone

from dtos.sale.sale_response import SaleResponseDTO
from dtos.sale.sale_create import SaleCreateDTO
from dtos.sale.sale_update import SaleUpdateDTO

from simulations.sales_data import sales_data
sales = sales_data

class SaleService:

    @staticmethod
    def get_sales():
        return sales

    @staticmethod
    def find_sale(sale_id: int):
        found_sale = None
        for sale in sales:
            if sale.id == sale_id:
                found_sale = sale

        if found_sale is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Sale not found"
            )

        return found_sale

    @staticmethod
    def create_sale(dto: SaleCreateDTO):
        new_id = len(sales) + 1

        folio = "VTA-" + str(new_id).zfill(4)

        now = datetime.now(timezone.utc)

        new_sale = SaleResponseDTO(
            id=new_id,
            folio=folio,
            location_id=dto.location_id,
            datetime=now,
            total=0.0,
            status="open",
            created_at=now,
            updated_at=now
        )

        sales.append(new_sale)

        return new_sale

    @staticmethod
    def update_sale(dto: SaleUpdateDTO):
        sale = SaleService.find_sale(sale_id=dto.id)

        sale.status = dto.status
        sale.updated_at = datetime.now(timezone.utc)

        return sale

    @staticmethod
    def recalculate_total(sale_id: int, details: list):
        sale = SaleService.find_sale(sale_id=sale_id)

        new_total = 0.0
        for detail in details:
            new_total = new_total + detail.subtotal

        sale.total = new_total
        sale.updated_at = datetime.now(timezone.utc)

        return sale

    @staticmethod
    def delete_sale(sale_id: int):
        sale = SaleService.find_sale(sale_id=sale_id)

        if sale.status != "open":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Only open sales can be deleted"
            )

        sales.remove(sale)

        return sale
