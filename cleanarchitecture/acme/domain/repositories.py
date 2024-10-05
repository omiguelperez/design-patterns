from abc import ABC, abstractmethod

from acme.domain.entities import LoanApplication


class ILoanApplicationRepository(ABC):
    @abstractmethod
    def save(self, application: "LoanApplication"):
        raise NotImplementedError
