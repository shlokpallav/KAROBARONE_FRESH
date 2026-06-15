from sqlalchemy.orm import Session

from app.models.store import Store
from app.schemas.store_schema import StoreCreate


def create_store(db: Session, payload: StoreCreate):
    store = Store(**payload.model_dump())

    db.add(store)
    db.commit()
    db.refresh(store)

    return store


def get_stores(db: Session):
    return db.query(Store).all()


def get_store_by_id(db: Session, store_id):
    return db.query(Store).filter(Store.id == store_id).first()