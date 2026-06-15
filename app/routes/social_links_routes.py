from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.controllers.social_link_controller import (
    create_social_link,
    get_social_links,
    get_social_link_by_id
)

from app.schemas.social_link_schema import (
    SocialLinkCreate
)

router = APIRouter(
    prefix="/social-links",
    tags=["Social Links"]
)


@router.post("/")
def create_social_link_route(
    payload: SocialLinkCreate,
    db: Session = Depends(get_db)
):
    return create_social_link(
        db,
        payload
    )


@router.get("/")
def get_social_links_route(
    db: Session = Depends(get_db)
):
    return get_social_links(db)


@router.get("/{social_link_id}")
def get_social_link_by_id_route(
    social_link_id: str,
    db: Session = Depends(get_db)
):
    return get_social_link_by_id(
        db,
        social_link_id
    )