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
        self.__approved_at: datetime | None = None
        self.__rejection_reasons: set[str] = set()

    @property
    def approved_at(self) -> datetime | None:
        if self.status is not ApplicationStatus.APPROVED:
            return None
        return self.__approved_at

    @approved_at.setter
    def approved_at(self, approved_at: datetime):
        if self.status is not ApplicationStatus.APPROVED:
            raise ValueError(
                "approved_at can only be set when the application is approved"
            )
        self.__approved_at = approved_at

    @property
    def rejection_reasons(self) -> list[str]:
        if self.status is not ApplicationStatus.REJECTED:
            return []
        return self.__rejection_reasons

    @rejection_reasons.setter
    def rejection_reasons(self, reasons: list[str]):
        if self.status is not ApplicationStatus.REJECTED:
            raise ValueError(
                "rejection_reasons can only be set when the application is rejected"
            )
        self.__rejection_reasons = reasons

    def approve(self):
        self.status = ApplicationStatus.APPROVED
        self.approved_at = datetime.now()

    def reject(self, reasons: list[str]):
        self.status = ApplicationStatus.REJECTED
        self.rejection_reasons = reasons


class LoanApplication(Application):
    pass


class CreditCardApplication(Application):
    pass
