from uuid import UUID
from typing import Optional

from pydantic import BaseModel


class SocialPlatformCreate(BaseModel):
    platform_code: str
    platform_name: str
    profile_url: Optional[str] = None
    icon_src: Optional[str] = None
    is_active: bool = True


class SocialPlatformResponse(BaseModel):
    id: UUID
    platform_code: str
    platform_name: str
    profile_url: Optional[str] = None
    icon_src: Optional[str] = None
    is_active: bool

    class Config:
        from_attributes = True