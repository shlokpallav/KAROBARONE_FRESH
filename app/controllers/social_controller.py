from sqlalchemy.orm import Session

from app.models.social_platform import SocialPlatform
from app.schemas.social_platform_schema import SocialPlatformCreate


def create_social_platform(
    db: Session,
    payload: SocialPlatformCreate
):
    social_platform = SocialPlatform(
        **payload.model_dump()
    )

    db.add(social_platform)
    db.commit()
    db.refresh(social_platform)

    return social_platform


def get_social_platforms(db: Session):
    return db.query(SocialPlatform).all()


def get_social_platform_by_id(
    db: Session,
    platform_id
):
    return (
        db.query(SocialPlatform)
        .filter(SocialPlatform.id == platform_id)
        .first()
    )