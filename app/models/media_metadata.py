import uuid

from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database import Base


class MediaMetadata(Base):
    __tablename__ = "media_metadata"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    media_file_id = Column(UUID(as_uuid=True), nullable=False)

    alt_text = Column(String(500))

    caption = Column(Text)

    title = Column(String(255))

    description = Column(Text)

    slug = Column(String(255))

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )