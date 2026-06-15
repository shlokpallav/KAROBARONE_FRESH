from sqlalchemy.orm import Session

from app.models.media_metadata import MediaMetadata

from app.schemas.media_metadata_schema import (
    MediaMetadataCreate
)


def create_media_metadata(
    db: Session,
    payload: MediaMetadataCreate
):
    media = MediaMetadata(
        **payload.model_dump()
    )

    db.add(media)
    db.commit()
    db.refresh(media)

    return media


def get_media_metadata(
    db: Session
):
    return db.query(
        MediaMetadata
    ).all()