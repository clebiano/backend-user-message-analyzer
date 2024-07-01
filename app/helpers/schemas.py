from typing import Any
from pydantic import BaseModel, Field, PositiveInt


class BaseSchemaMixin(BaseModel):
    class Config:
        extra = 'forbid'
        from_attributes = True
        arbitrary_types_allowed = True
        populate_by_name = True


class Page(BaseSchemaMixin):
    limit: PositiveInt
    offset: int = Field(..., ge=0)
    count: int = Field(..., ge=0)
    # max_limit: PositiveInt


class Meta(BaseSchemaMixin):
    page: Page
    # links: dict[str, str]


class CollectionResponse(BaseSchemaMixin):
    meta: Meta
    results: list[Any]
