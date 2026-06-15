from uuid import UUID
from typing import Optional

from pydantic import BaseModel


class WebsiteThemeCreate(BaseModel):
    theme_name: str
    theme_code: str
    preview_image_id: Optional[UUID] = None
    is_active: bool = True


class WebsiteThemeResponse(BaseModel):
    id: UUID
    theme_name: str
    theme_code: str

    class Config:
        from_attributes = True