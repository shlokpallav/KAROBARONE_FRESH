from uuid import UUID
from datetime import time

from pydantic import BaseModel


class StoreBusinessHoursCreate(BaseModel):
    store_id: UUID
    closed_day_of_year: int
    open_time: time
    close_time: time
    physical_store_present: bool


class StoreBusinessHoursResponse(BaseModel):
    id: UUID
    store_id: UUID

    class Config:
        from_attributes = True