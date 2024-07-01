from app.helpers.schemas import BaseSchemaMixin, CollectionResponse
from pydantic import Field


class FileOut(BaseSchemaMixin):
    file_name: str = Field(title='File name')
    size: int = Field(title='Size')

    # class Config:
    #     schema_extra = {'example': sku_collection_response_example}


class FileCollectionOut(CollectionResponse):
    results: list[FileOut]

    # class Config:
    #     schema_extra = {'example': sku_collection_response_example}
