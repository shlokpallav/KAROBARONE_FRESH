from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.controllers.store_branding_controller import (
    create_store_branding,
    get_store_branding
)

from app.schemas.store_branding_schema import (
    StoreBrandingCreate
)

router = APIRouter(
    prefix="/store-branding",
    tags=["Store Branding"]
)


@router.post("/")
def create_store_branding_route(
    payload: StoreBrandingCreate,
    db: Session = Depends(get_db)
):
    return create_store_branding(
        db,
        payload
    )


@router.get("/")
def get_store_branding_route(
    db: Session = Depends(get_db)
):
    return get_store_branding(db)