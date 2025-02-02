from decimal import Decimal

from pydantic import BaseModel, Field, HttpUrl, field_serializer

from app.models.product import Product
from app.schemas.base import BaseListResponse


class ProductCreateRequest(BaseModel):
    name: str
    description: str | None = None
    image: HttpUrl | None = None
    price: Decimal = Field(max_digits=12, decimal_places=2)
    stock: int | None = 0

    @field_serializer("image")
    def validate_image(self, image: HttpUrl, _info):
        return str(image)


class ProductCreateResponse(Product):
    pass


class ProductListResponseItem(Product):
    pass


class ProductListResponse(BaseListResponse):
    results: list[ProductListResponseItem]


class ProductDetailResponse(Product):
    pass


class ProductUpdateRequest(ProductCreateRequest):
    name: str | None = None
    description: str | None = None
    image: HttpUrl | None = None
    price: Decimal | None = Field(default=None, max_digits=12, decimal_places=2)
    stock: int | None = None
