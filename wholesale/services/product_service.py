from fastapi import HTTPException
from starlette import status
from datetime import datetime, timezone

from dtos.product.product_response import ProductResponseDTO
from dtos.product.product_create import ProductCreateDTO
from dtos.product.product_update import ProductUpdateDTO

from simulations.products_data import products_data
products = products_data

class ProductService:

    @staticmethod
    def get_products():
        active_products = []
        for product in products:
            if product.active == True:
                active_products.append(product)
        return active_products

    @staticmethod
    def find_product(product_id: int):
        found_product = None
        for product in products:
            if product.id == product_id:
                found_product = product

        if found_product is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found"
            )

        return found_product

    @staticmethod
    def create_product(dto: ProductCreateDTO):
        new_id = len(products) + 1

        now = datetime.now(timezone.utc)

        new_product = ProductResponseDTO(
            id=new_id,
            barcode=dto.barcode,
            name=dto.name,
            description=dto.description,
            brand=dto.brand,
            price=dto.price,
            stock=dto.stock,
            active=True,
            created_at=now,
            updated_at=now
        )

        products.append(new_product)

        return new_product

    @staticmethod
    def update_product(dto: ProductUpdateDTO):
        product = ProductService.find_product(product_id=dto.id)

        product.barcode = dto.barcode
        product.name = dto.name
        product.description = dto.description
        product.brand = dto.brand
        product.price = dto.price
        product.stock = dto.stock
        product.updated_at = datetime.now(timezone.utc)

        return product

    @staticmethod
    def delete_product(product_id: int):
        product = ProductService.find_product(product_id=product_id)

        product.active = False
        product.updated_at = datetime.now(timezone.utc)

        return product
