import uuid

from sqlalchemy import Column, String, Text, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database import Base


class SeoMetadata(Base):
    __tablename__ = "seo_metadata"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    tenant_id = Column(UUID(as_uuid=True), nullable=False)

    entity_id = Column(UUID(as_uuid=True))

    meta_title = Column(String(255))

    meta_description = Column(Text)

    canonical_url = Column(Text)

    slug = Column(String(255))

    robots_index = Column(Boolean, default=True)

    robots_follow = Column(Boolean, default=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )