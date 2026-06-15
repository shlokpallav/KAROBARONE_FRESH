from sqlalchemy.orm import Session

from app.models.store_business_hours import StoreBusinessHours
from app.schemas.store_business_hours_schema import (
    StoreBusinessHoursCreate
)


def create_store_business_hours(
    db: Session,
    payload: StoreBusinessHoursCreate
):
    business_hours = StoreBusinessHours(
        **payload.model_dump()
    )

    db.add(business_hours)
    db.commit()
    db.refresh(business_hours)

    return business_hours


def get_store_business_hours(
    db: Session
):
    return db.query(
        StoreBusinessHours
    ).all()