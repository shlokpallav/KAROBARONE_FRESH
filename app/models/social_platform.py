import uuid

from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database import Base


class SocialPlatform(Base):
    __tablename__ = "social_platforms"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    platform_code = Column(String(100), nullable=False)

    platform_name = Column(String(255), nullable=False)

    profile_url = Column(String)

    icon_src = Column(String(100))

    is_active = Column(Boolean, default=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )