from typing import Optional

from acme.domain.entities.application import ApplicationStatus, CreditCardApplication
from acme.domain.entities.approvers import BankApprover
from acme.domain.repositories import ICreditCardApplicationRepository
from acme.domain.services.credit_score import BankCreditScoreService
from acme.domain.services.criminal_record import BankCriminalRecordService
from acme.domain.specs import (
    HasNoCriminalRecord,
    HasNotAppliedForCreditCardInTheLast6Months,
    IsCreditScoreAcceptable,
)
from pydantic import BaseModel


class CreditCardApplicationRequest(BaseModel):
    ssn: str
    amount: float


class CreditCardApplicationResponse(BaseModel):
    ssn: str
    amount: float
    credit_score: Optional[int]
    status: ApplicationStatus


class CreditCardApplyUseCase:
    def __init__(
        self,
        credit_card_application_repository: "ICreditCardApplicationRepository",
        bank_credit_score_service: "BankCreditScoreService",
        bank_criminal_record_service: "BankCriminalRecordService",
    ):
        self.__credit_card_application_repository = credit_card_application_repository

        self.__bank_credit_score_service = bank_credit_score_service
        self.__bank_criminal_record_service = bank_criminal_record_service

    def execute(
        self, request: "CreditCardApplicationRequest"
    ) -> "CreditCardApplicationResponse":
        application = CreditCardApplication(request.ssn, request.amount)

        bank_approver = BankApprover()
        bank_approver.let_him_know_requirements_to_approve_application(
            IsCreditScoreAcceptable(self.__bank_credit_score_service),
            HasNoCriminalRecord(self.__bank_criminal_record_service),
            HasNotAppliedForCreditCardInTheLast6Months(
                self.__credit_card_application_repository
            ),
        )

        bank_approver.review_application(application)

        self.__credit_card_application_repository.save(application)

        return CreditCardApplicationResponse(
            ssn=application.ssn,
            amount=application.amount,
            credit_score=application.credit_score,
            status=application.status,
        )
