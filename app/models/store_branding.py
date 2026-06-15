import uuid

from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database import Base


class StoreBranding(Base):
    __tablename__ = "store_branding"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    store_id = Column(UUID(as_uuid=True), nullable=False)

    primary_color = Column(String(20))
    secondary_color = Column(String(20))
    accent_color = Column(String(20))

    font_family = Column(String(100))

    custom_css = Column(Text)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )