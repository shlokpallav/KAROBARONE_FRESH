from sqlalchemy.orm import Session

from app.models.section import Section
from app.schemas.section_schema import SectionCreate


def create_section(
    db: Session,
    payload: SectionCreate
):
    section = Section(
        **payload.model_dump()
    )

    db.add(section)
    db.commit()
    db.refresh(section)

    return section


def get_sections(
    db: Session
):
    return db.query(
        Section
    ).all()