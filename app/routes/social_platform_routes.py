from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.controllers.social_controller import (
    create_social_platform,
    get_social_platforms,
    get_social_platform_by_id
)

from app.schemas.social_platform_schema import (
    SocialPlatformCreate
)

router = APIRouter(
    prefix="/social-platforms",
    tags=["Social Platforms"]
)


@router.post("/")
def create_social_platform_route(
    payload: SocialPlatformCreate,
    db: Session = Depends(get_db)
):
    return create_social_platform(db, payload)


@router.get("/")
def get_social_platforms_route(
    db: Session = Depends(get_db)
):
    return get_social_platforms(db)


@router.get("/{platform_id}")
def get_social_platform_by_id_route(
    platform_id: str,
    db: Session = Depends(get_db)
):
    return get_social_platform_by_id(
        db,
        platform_id
    )