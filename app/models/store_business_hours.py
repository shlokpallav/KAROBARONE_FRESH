import uuid

from sqlalchemy import Column, Boolean, SmallInteger, Time, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database import Base


class StoreBusinessHours(Base):
    __tablename__ = "store_business_hours"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    store_id = Column(UUID(as_uuid=True), nullable=False)

    closed_day_of_year = Column(SmallInteger)

    open_time = Column(Time)

    close_time = Column(Time)

    physical_store_present = Column(Boolean)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )