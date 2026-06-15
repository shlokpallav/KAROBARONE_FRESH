from sqlalchemy.orm import Session

from app.models.seo_metadata import SeoMetadata

from app.schemas.seo_metadata_schema import (
    SeoMetadataCreate
)


def create_seo_metadata(
    db: Session,
    payload: SeoMetadataCreate
):
    seo = SeoMetadata(
        **payload.model_dump()
    )

    db.add(seo)
    db.commit()
    db.refresh(seo)

    return seo


def get_seo_metadata(
    db: Session
):
    return db.query(
        SeoMetadata
    ).all()