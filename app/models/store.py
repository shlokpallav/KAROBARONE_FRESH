import uuid

from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database import Base


class Store(Base):
    __tablename__ = "stores"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    tenant_id = Column(UUID(as_uuid=True), nullable=False)
    store_slug = Column(String(255), unique=True, nullable=False)

    tagline = Column(String(500))

    marquee_text_1 = Column(Text)
    marquee_text_2 = Column(Text)
    marquee_text_3 = Column(Text)
    marquee_text_4 = Column(Text)
    marquee_text_5 = Column(Text)

    logo_media_src = Column(UUID(as_uuid=True))
    favicon_media_src = Column(UUID(as_uuid=True))

    hero_media_src_1 = Column(UUID(as_uuid=True))
    hero_media_src_2 = Column(UUID(as_uuid=True))
    hero_media_src_3 = Column(UUID(as_uuid=True))

    about_promoter = Column(Text)
    about_promoter_image = Column(UUID(as_uuid=True))

    about_company = Column(Text)
    about_company_image = Column(UUID(as_uuid=True))

    about_certifications = Column(Text)
    about_certifications_image = Column(UUID(as_uuid=True))

    why_choose_us_1 = Column(Text)
    why_choose_us_2 = Column(Text)
    why_choose_us_3 = Column(Text)
    why_choose_us_4 = Column(Text)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )