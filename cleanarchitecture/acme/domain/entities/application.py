from abc import ABC
from datetime import datetime
from enum import Enum


class ApplicationStatus(Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


class Application(ABC):
    def __init__(self, ssn: str, amount: float):
        self.ssn = ssn
        self.amount = amount
        self.credit_score: int | None = None
        self.status = ApplicationStatus.PENDING
        self.approved_at: datetime | None = None
        self.rejection_reasons: set[str] = []

    def approve(self):
        self.status = ApplicationStatus.APPROVED
        self.approved_at = datetime.now()

    def reject(self, reasons: list[str]):
        self.status = ApplicationStatus.REJECTED
        self.rejection_reasons.extend(reasons)


class LoanApplication(Application):
    pass


class CreditCardApplication(Application):
    pass
