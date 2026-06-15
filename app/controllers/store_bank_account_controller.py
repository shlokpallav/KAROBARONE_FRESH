from sqlalchemy.orm import Session

from app.models.store_bank_account import StoreBankAccount

from app.schemas.store_bank_account_schema import (
    StoreBankAccountCreate
)


def create_store_bank_account(
    db: Session,
    payload: StoreBankAccountCreate
):
    account = StoreBankAccount(
        **payload.model_dump()
    )

    db.add(account)
    db.commit()
    db.refresh(account)

    return account


def get_store_bank_accounts(
    db: Session
):
    return db.query(
        StoreBankAccount
    ).all()