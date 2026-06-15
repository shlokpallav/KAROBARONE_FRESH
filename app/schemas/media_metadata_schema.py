from uuid import UUID
from typing import Optional

from pydantic import BaseModel


class MediaMetadataCreate(BaseModel):
    media_file_id: UUID

    alt_text: Optional[str] = None

    caption: Optional[str] = None

    title: Optional[str] = None

    description: Optional[str] = None

    slug: Optional[str] = None


class MediaMetadataResponse(BaseModel):
    id: UUID

    class Config:
        from_attributes = True