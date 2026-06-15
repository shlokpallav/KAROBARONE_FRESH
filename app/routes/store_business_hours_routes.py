from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.controllers.store_business_hours_controller import (
    create_store_business_hours,
    get_store_business_hours
)

from app.schemas.store_business_hours_schema import (
    StoreBusinessHoursCreate
)

router = APIRouter(
    prefix="/store-business-hours",
    tags=["Store Business Hours"]
)


@router.post("/")
def create_store_business_hours_route(
    payload: StoreBusinessHoursCreate,
    db: Session = Depends(get_db)
):
    return create_store_business_hours(
        db,
        payload
    )


@router.get("/")
def get_store_business_hours_route(
    db: Session = Depends(get_db)
):
    return get_store_business_hours(db)