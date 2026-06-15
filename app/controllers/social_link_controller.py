from sqlalchemy.orm import Session

from app.models.social_link import SocialLink
from app.schemas.social_link_schema import SocialLinkCreate


def create_social_link(
    db: Session,
    payload: SocialLinkCreate
):
    social_link = SocialLink(
        **payload.model_dump()
    )

    db.add(social_link)
    db.commit()
    db.refresh(social_link)

    return social_link


def get_social_links(db: Session):
    return db.query(SocialLink).all()


def get_social_link_by_id(
    db: Session,
    social_link_id
):
    return (
        db.query(SocialLink)
        .filter(SocialLink.id == social_link_id)
        .first()
    )