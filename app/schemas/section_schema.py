from uuid import UUID
from typing import Optional

from pydantic import BaseModel


class SectionCreate(BaseModel):
    store_id: UUID
    plan_id: Optional[UUID] = None
    section_name: str


class SectionResponse(BaseModel):
    id: UUID
    section_name: str

    class Config:
        from_attributes = True
