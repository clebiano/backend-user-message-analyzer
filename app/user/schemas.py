from app.helpers.schemas import BaseSchemaMixin


class UserOut(BaseSchemaMixin):
    pass


class UserCollectionOut(BaseSchemaMixin):
    results: list[UserOut]

    # class Config:
    #     schema_extra = {'example': sku_collection_response_example}
