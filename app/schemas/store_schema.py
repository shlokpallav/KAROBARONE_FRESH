from uuid import UUID
from typing import Optional

from pydantic import BaseModel


class StoreCreate(BaseModel):
    tenant_id: UUID
    store_slug: str
    tagline: Optional[str] = None

class StoreResponse(BaseModel):
    id: UUID
    pan_number: UUID
    store_slug: str
    tagline: Optional[str] = None

    class Config:
        from_attributes = True