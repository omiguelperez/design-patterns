from enum import Enum

from acme.domain.specs.loan_application import LoanSpecification


class BankFinancialEmployee:
    def __init__(self):
        self.__bank_requirements_to_approve_loan = []

    def let_him_know_requirements_to_approve_loan(
        self, *requirements: list["LoanSpecification"]
    ):
        self.__bank_requirements_to_approve_loan.extend(requirements)

    def apply_loan(self, application: "LoanApplication"):
        all_requirements_met = all(
            requirement.is_satisfied_by(application)
            for requirement in self.__bank_requirements_to_approve_loan
        )
        if all_requirements_met:
            application.approve()
        else:
            application.reject()


class LoanApplicationStatus(Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


class LoanApplication:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.credit_score: int | None = None
        self.status = LoanApplicationStatus.PENDING

    def approve(self):
        self.status = LoanApplicationStatus.APPROVED

    def reject(self):
        self.status = LoanApplicationStatus.REJECTED
