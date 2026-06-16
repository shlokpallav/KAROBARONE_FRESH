from uuid import UUID
from pydantic import BaseModel


class SocialLinkCreate(BaseModel):
    store_id: UUID
    platform_id: UUID
    profile_url: str
    is_active: bool = True


class SocialLinkResponse(BaseModel):
    id: UUID
    store_id: UUID
    platform_id: UUID
    profile_url: str
    is_active: bool

    class Config:
        from_attributes = True
