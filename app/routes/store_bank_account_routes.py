from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.controllers.store_bank_account_controller import (
    create_store_bank_account,
    get_store_bank_accounts
)

from app.schemas.store_bank_account_schema import (
    StoreBankAccountCreate
)

router = APIRouter(
    prefix="/store-bank-accounts",
    tags=["Store Bank Accounts"]
)


@router.post("/")
def create_store_bank_account_route(
    payload: StoreBankAccountCreate,
    db: Session = Depends(get_db)
):
    return create_store_bank_account(
        db,
        payload
    )


@router.get("/")
def get_store_bank_accounts_route(
    db: Session = Depends(get_db)
):
    return get_store_bank_accounts(db)