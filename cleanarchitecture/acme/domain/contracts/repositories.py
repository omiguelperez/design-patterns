from abc import ABC, abstractmethod
from datetime import datetime

from acme.domain.entities.application import CreditCardApplication, LoanApplication


class ILoanApplicationRepository(ABC):
    @abstractmethod
    def save(self, application: "LoanApplication"):
        raise NotImplementedError


class ICreditCardApplicationRepository(ABC):
    @abstractmethod
    def save(self, application: "CreditCardApplication") -> int:
        raise NotImplementedError

    @abstractmethod
    def fetch_since_for_applicant(
        self, since: datetime, applicant_ssn: str
    ) -> list["CreditCardApplication"]:
        raise NotImplementedError


class IEligibilityCriteriaRepository(ABC):
    @abstractmethod
    def fetch_credit_card_approval_criteria_types(self) -> list[str]:
        raise NotImplementedError

    @abstractmethod
    def fetch_loan_approval_criteria_types(self) -> list[str]:
        raise NotImplementedError
