import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from app.database import Base


class StoreBankAccount(Base):
    __tablename__ = "store_bank_accounts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    store_id = Column(UUID(as_uuid=True), nullable=False)

    account_holder_name = Column(String(255))

    bank_name = Column(String(255))

    branch_name = Column(String(255))

    account_number_masked = Column(String(50))

    ifsc_code = Column(String(20))

    account_type = Column(String(50))

    verification_status = Column(String(50))
