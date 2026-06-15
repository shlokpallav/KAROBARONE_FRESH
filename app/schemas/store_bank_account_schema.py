from uuid import UUID
from typing import Optional

from pydantic import BaseModel


class StoreBankAccountCreate(BaseModel):
    pan_number: UUID

    account_holder_name: str

    bank_name: str

    branch_name: Optional[str] = None

    account_number_masked: str

    ifsc_code: str

    account_type: str

    verification_status: str = "PENDING"


class StoreBankAccountResponse(BaseModel):
    id: UUID
    pan_number: UUID

    class Config:
        from_attributes = True