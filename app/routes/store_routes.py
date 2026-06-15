from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.controllers.store_controller import (
    create_store,
    get_stores,
    get_store_by_id
)
from app.schemas.store_schema import StoreCreate

router = APIRouter(
    prefix="/stores",
    tags=["Stores"]
)


@router.post("/")
def create_store_route(
    payload: StoreCreate,
    db: Session = Depends(get_db)
):
    return create_store(db, payload)


@router.get("/")
def get_stores_route(
    db: Session = Depends(get_db)
):
    return get_stores(db)


@router.get("/{store_id}")
def get_store_by_id_route(
    store_id: str,
    db: Session = Depends(get_db)
):
    return get_store_by_id(db, store_id)