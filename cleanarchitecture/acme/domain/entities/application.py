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

    def approve(self):
        self.status = ApplicationStatus.APPROVED
        self.approved_at = datetime.now()

    def reject(self):
        self.status = ApplicationStatus.REJECTED


class LoanApplication(Application):
    pass


class CreditCardApplication(Application):
    pass
