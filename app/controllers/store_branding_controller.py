from sqlalchemy.orm import Session

from app.models.store_branding import StoreBranding
from app.schemas.store_branding_schema import (
    StoreBrandingCreate
)


def create_store_branding(
    db: Session,
    payload: StoreBrandingCreate
):
    branding = StoreBranding(
        **payload.model_dump()
    )

    db.add(branding)
    db.commit()
    db.refresh(branding)

    return branding


def get_store_branding(
    db: Session
):
    return db.query(
        StoreBranding
    ).all()