from abc import ABC
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

    def approve(self):
        self.status = ApplicationStatus.APPROVED

    def reject(self):
        self.status = ApplicationStatus.REJECTED


class LoanApplication(Application):
    pass
