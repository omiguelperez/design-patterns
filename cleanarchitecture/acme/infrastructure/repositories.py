from acme.domain.entities import LoanApplication
from acme.domain.repositories import ILoanApplicationRepository


class InMemoryLoanApplicationRepository(ILoanApplicationRepository):
    def __init__(self):
        self.__applications = []

    def save(self, application: "LoanApplication"):
        self.__applications.append(application)
