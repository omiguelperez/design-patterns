from datetime import datetime

from acme.domain.entities.application import LoanApplication
from acme.domain.repositories import ILoanApplicationRepository


class InMemoryLoanApplicationRepository(ILoanApplicationRepository):
    def __init__(self):
        self.__applications = []

    def save(self, application: "LoanApplication"):
        self.__applications.append(application)


class InMemoryCreditCardApplicationRepository(ILoanApplicationRepository):
    def __init__(self):
        self.__applications = []

    def save(self, application: "LoanApplication"):
        self.__applications.append(application)

    def fetch_since_for_applicant(self, since: datetime, applicant_ssn: str):
        return [
            application
            for application in self.__applications
            if application.ssn == applicant_ssn and application.approved_at >= since
        ]
