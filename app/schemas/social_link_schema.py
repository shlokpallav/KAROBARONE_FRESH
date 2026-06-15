from uuid import UUID
from pydantic import BaseModel


class SocialLinkCreate(BaseModel):
    pan_number: UUID
    platform_id: UUID
    profile_url: str
    is_active: bool = True


class SocialLinkResponse(BaseModel):
    id: UUID
    pan_number: UUID
    platform_id: UUID
    profile_url: str
    is_active: bool

    class Config:
        from_attributes = True