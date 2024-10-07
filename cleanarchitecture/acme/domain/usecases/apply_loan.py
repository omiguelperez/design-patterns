from typing import Optional

from acme.domain.entities.application import ApplicationStatus, LoanApplication
from acme.domain.entities.approvers import BankApprover
from acme.domain.factories import EligibilityCriteriaFactory
from acme.domain.repositories import (
    IEligibilityCriteriaRepository,
    ILoanApplicationRepository,
)
from pydantic import BaseModel


class LoanApplicationRequest(BaseModel):
    ssn: str
    amount: float


class LoanApplicationResponse(BaseModel):
    ssn: str
    amount: float
    credit_score: Optional[int]
    status: ApplicationStatus
    rejection_reasons: list[str]


class LoanApplyUseCase:
    def __init__(
        self,
        loan_application_repository: ILoanApplicationRepository,
        elibility_criteria_repository: "IEligibilityCriteriaRepository",
        elibility_criteria_factory: "EligibilityCriteriaFactory",
    ):
        self.__loan_application_repository = loan_application_repository
        self.__eligibility_criteria_repository = elibility_criteria_repository

        self.__eligibility_criteria_factory = elibility_criteria_factory

    def execute(self, request: "LoanApplicationRequest") -> "LoanApplicationResponse":
        application = LoanApplication(request.ssn, request.amount)
        bank_employee = BankApprover()

        approval_criteria_types = (
            self.__eligibility_criteria_repository.fetch_loan_approval_criteria_types()
        )
        approval_criteria = self.__eligibility_criteria_factory.create_many(approval_criteria_types)
        bank_employee.add_approval_criteria(approval_criteria=approval_criteria)

        bank_employee.review_application(application)

        self.__loan_application_repository.save(application)

        return LoanApplicationResponse(
            ssn=application.ssn,
            amount=application.amount,
            credit_score=application.credit_score,
            status=application.status,
            rejection_reasons=application.rejection_reasons,
        )
