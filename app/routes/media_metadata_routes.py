from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.controllers.media_controller import (
    create_media_metadata,
    get_media_metadata
)

from app.schemas.media_metadata_schema import (
    MediaMetadataCreate
)

router = APIRouter(
    prefix="/media-metadata",
    tags=["Media Metadata"]
)


@router.post("/")
def create_media_metadata_route(
    payload: MediaMetadataCreate,
    db: Session = Depends(get_db)
):
    return create_media_metadata(
        db,
        payload
    )


@router.get("/")
def get_media_metadata_route(
    db: Session = Depends(get_db)
):
    return get_media_metadata(db)