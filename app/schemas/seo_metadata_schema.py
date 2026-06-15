from uuid import UUID
from typing import Optional

from pydantic import BaseModel


class SeoMetadataCreate(BaseModel):
    tenant_id: UUID

    entity_id: Optional[UUID] = None

    meta_title: Optional[str] = None

    meta_description: Optional[str] = None

    canonical_url: Optional[str] = None

    slug: Optional[str] = None

    robots_index: bool = True

    robots_follow: bool = True


class SeoMetadataResponse(BaseModel):
    id: UUID

    class Config:
        from_attributes = True