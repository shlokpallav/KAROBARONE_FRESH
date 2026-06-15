from uuid import UUID
from typing import Optional

from pydantic import BaseModel


class StoreBrandingCreate(BaseModel):
    store_id: UUID

    primary_color: Optional[str] = None
    secondary_color: Optional[str] = None
    accent_color: Optional[str] = None

    font_family: Optional[str] = None

    custom_css: Optional[str] = None


class StoreBrandingResponse(BaseModel):
    id: UUID
    store_id: UUID

    class Config:
        from_attributes = True