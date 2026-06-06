from fastapi import APIRouter
from starlette import status
from typing import List

from services.sale_service import SaleService
from services.sale_detail_service import SaleDetailService
from dtos.sale.sale_response import SaleResponseDTO
from dtos.sale.sale_create import SaleCreateDTO
from dtos.sale.sale_update import SaleUpdateDTO
from dtos.sale_detail.sale_detail_response import SaleDetailResponseDTO
from dtos.sale_detail.sale_detail_create import SaleDetailCreateDTO
from dtos.sale_detail.sale_detail_update import SaleDetailUpdateDTO

router = APIRouter(
    prefix="/sales",
    tags=["Sales"]
)

@router.get("/", response_model=List[SaleResponseDTO], status_code=status.HTTP_200_OK)
def get_sales():
    return SaleService.get_sales()

@router.get("/{sale_id}", response_model=SaleResponseDTO, status_code=status.HTTP_200_OK)
def find_sale(sale_id: int):
    return SaleService.find_sale(sale_id=sale_id)

@router.post("/", response_model=SaleResponseDTO, status_code=status.HTTP_201_CREATED)
def create_sale(data: SaleCreateDTO):
    return SaleService.create_sale(dto=data)

@router.put("/", response_model=SaleResponseDTO, status_code=status.HTTP_202_ACCEPTED)
def update_sale(data: SaleUpdateDTO):
    return SaleService.update_sale(dto=data)

@router.delete("/{sale_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sale(sale_id: int):
    SaleService.delete_sale(sale_id=sale_id)


@router.get("/{sale_id}/details", response_model=List[SaleDetailResponseDTO], status_code=status.HTTP_200_OK)
def get_details(sale_id: int):
    return SaleDetailService.get_details_by_sale(sale_id=sale_id)

@router.post("/details", response_model=SaleDetailResponseDTO, status_code=status.HTTP_201_CREATED)
def create_detail(data: SaleDetailCreateDTO):
    detail = SaleDetailService.create_detail(dto=data)
    details = SaleDetailService.get_details_by_sale(sale_id=data.sale_id)
    SaleService.recalculate_total(sale_id=data.sale_id, details=details)
    return detail

@router.put("/details", response_model=SaleDetailResponseDTO, status_code=status.HTTP_202_ACCEPTED)
def update_detail(data: SaleDetailUpdateDTO):
    detail = SaleDetailService.update_detail(dto=data)
    details = SaleDetailService.get_details_by_sale(sale_id=detail.sale_id)
    SaleService.recalculate_total(sale_id=detail.sale_id, details=details)
    return detail

@router.delete("/details/{detail_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_detail(detail_id: int):
    detail = SaleDetailService.delete_detail(detail_id=detail_id)
    details = SaleDetailService.get_details_by_sale(sale_id=detail.sale_id)
    SaleService.recalculate_total(sale_id=detail.sale_id, details=details)
