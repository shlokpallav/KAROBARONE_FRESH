from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.controllers.seo_controller import (
    create_seo_metadata,
    get_seo_metadata
)

from app.schemas.seo_metadata_schema import (
    SeoMetadataCreate
)

router = APIRouter(
    prefix="/seo-metadata",
    tags=["SEO Metadata"]
)


@router.post("/")
def create_seo_metadata_route(
    payload: SeoMetadataCreate,
    db: Session = Depends(get_db)
):
    return create_seo_metadata(
        db,
        payload
    )


@router.get("/")
def get_seo_metadata_route(
    db: Session = Depends(get_db)
):
    return get_seo_metadata(db)