import uuid

from sqlalchemy import Column, Boolean, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database import Base


class SocialLink(Base):
    __tablename__ = "social_links"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    store_id = Column(UUID(as_uuid=True), nullable=False)

    platform_id = Column(UUID(as_uuid=True), nullable=False)

    profile_url = Column(Text)

    is_active = Column(Boolean, default=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
