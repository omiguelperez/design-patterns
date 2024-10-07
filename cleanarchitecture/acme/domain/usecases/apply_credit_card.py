from typing import Optional

from acme.domain.contracts.repositories import (
    ICreditCardApplicationRepository,
    IEligibilityCriteriaRepository,
)
from acme.domain.entities.application import ApplicationStatus, CreditCardApplication
from acme.domain.entities.approvers import BankApprover
from acme.domain.factories import EligibilityCriteriaFactory
from pydantic import BaseModel


class CreditCardApplicationRequest(BaseModel):
    ssn: str
    amount: float


class CreditCardApplicationResponse(BaseModel):
    ssn: str
    amount: float
    credit_score: Optional[int]
    status: ApplicationStatus
    rejection_reasons: list[str]


class CreditCardApplyUseCase:
    def __init__(
        self,
        credit_card_application_repository: "ICreditCardApplicationRepository",
        elibility_criteria_repository: "IEligibilityCriteriaRepository",
        elibility_criteria_factory: "EligibilityCriteriaFactory",
    ):
        self.__credit_card_application_repository = credit_card_application_repository
        self.__eligibility_criteria_repository = elibility_criteria_repository

        self.__eligibility_criteria_factory = elibility_criteria_factory

    def execute(self, request: "CreditCardApplicationRequest") -> "CreditCardApplicationResponse":
        application = CreditCardApplication(request.ssn, request.amount)
        bank_approver = BankApprover()

        aproval_criteria_types = (
            self.__eligibility_criteria_repository.fetch_credit_card_approval_criteria_types()
        )
        approval_criteria = self.__eligibility_criteria_factory.create_many(aproval_criteria_types)
        bank_approver.add_approval_criteria(approval_criteria=approval_criteria)

        bank_approver.review_application(application)

        self.__credit_card_application_repository.save(application)

        return CreditCardApplicationResponse(
            ssn=application.ssn,
            amount=application.amount,
            credit_score=application.credit_score,
            status=application.status,
            rejection_reasons=application.rejection_reasons,
        )
