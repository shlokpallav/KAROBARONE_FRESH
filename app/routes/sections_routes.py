from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.controllers.section_controller import (
    create_section,
    get_sections
)

from app.schemas.section_schema import (
    SectionCreate
)

router = APIRouter(
    prefix="/sections",
    tags=["Sections"]
)


@router.post("/")
def create_section_route(
    payload: SectionCreate,
    db: Session = Depends(get_db)
):
    return create_section(
        db,
        payload
    )


@router.get("/")
def get_sections_route(
    db: Session = Depends(get_db)
):
    return get_sections(db)