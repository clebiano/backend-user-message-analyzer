from pydantic import BaseModel


class BaseSchemaMixin(BaseModel):
    class Config:
        extra = 'forbid'
        from_attributes = True
        arbitrary_types_allowed = True
        populate_by_name = True
