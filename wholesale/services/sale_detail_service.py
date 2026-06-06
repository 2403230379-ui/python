from fastapi import HTTPException
from starlette import status

from dtos.sale_detail.sale_detail_response import SaleDetailResponseDTO
from dtos.sale_detail.sale_detail_create import SaleDetailCreateDTO
from dtos.sale_detail.sale_detail_update import SaleDetailUpdateDTO

from services.product_service import ProductService

from simulations.sale_details_data import sale_details_data
sale_details = sale_details_data

class SaleDetailService:

    @staticmethod
    def get_details_by_sale(sale_id: int):
        result = []
        for detail in sale_details:
            if detail.sale_id == sale_id:
                result.append(detail)
        return result

    @staticmethod
    def find_detail(detail_id: int):
        found_detail = None
        for detail in sale_details:
            if detail.id == detail_id:
                found_detail = detail

        if found_detail is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Sale detail not found"
            )

        return found_detail

    @staticmethod
    def create_detail(dto: SaleDetailCreateDTO):
        new_id = len(sale_details) + 1

        product = ProductService.find_product(product_id=dto.product_id)

        if product.stock < dto.quantity:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Not enough stock"
            )

        unit_price = product.price
        subtotal = unit_price * dto.quantity

        new_detail = SaleDetailResponseDTO(
            id=new_id,
            sale_id=dto.sale_id,
            product_id=dto.product_id,
            quantity=dto.quantity,
            unit_price=unit_price,
            subtotal=subtotal
        )

        product.stock = product.stock - dto.quantity

        sale_details.append(new_detail)

        return new_detail

    @staticmethod
    def update_detail(dto: SaleDetailUpdateDTO):
        detail = SaleDetailService.find_detail(detail_id=dto.id)

        product = ProductService.find_product(product_id=detail.product_id)

        product.stock = product.stock + detail.quantity

        if product.stock < dto.quantity:
            product.stock = product.stock - detail.quantity
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Not enough stock"
            )

        product.stock = product.stock - dto.quantity

        detail.quantity = dto.quantity
        detail.subtotal = detail.unit_price * dto.quantity

        return detail

    @staticmethod
    def delete_detail(detail_id: int):
        detail = SaleDetailService.find_detail(detail_id=detail_id)

        product = ProductService.find_product(product_id=detail.product_id)

        product.stock = product.stock + detail.quantity

        sale_details.remove(detail)

        return detail
