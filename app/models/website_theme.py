import uuid

from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database import Base


class WebsiteTheme(Base):
    __tablename__ = "website_themes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    theme_name = Column(String(255), nullable=False)

    theme_code = Column(String(100), nullable=False)

    preview_image_id = Column(UUID(as_uuid=True))

    is_active = Column(Boolean, default=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )