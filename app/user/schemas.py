from pydantic import Field

from app.helpers.schemas import BaseSchemaMixin, CollectionResponse


class UserOut(BaseSchemaMixin):
    username: str = Field(title="Username")
    folder: str = Field(title="Folder")
    number_messages: int = Field(title="Total messages", alias='numberMessages')
    size: int = Field(title="Message size")


class UserCollectionOut(CollectionResponse):
    results: list[UserOut]

    # class Config:
    #     schema_extra = {'example': sku_collection_response_example}
