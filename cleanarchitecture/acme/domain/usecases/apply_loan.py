from typing import Optional

from acme.domain.entities.application import ApplicationStatus, LoanApplication
from acme.domain.entities.approvers import BankApprover
from acme.domain.repositories import ILoanApplicationRepository
from acme.domain.services.credit_score import BankCreditScoreService
from acme.domain.services.criminal_record import BankCriminalRecordService
from acme.domain.specs import HasNoCriminalRecord, IsCreditScoreAcceptable
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
        bank_credit_score_service: BankCreditScoreService,
        bank_criminal_record_service: BankCriminalRecordService,
    ):
        self.__loan_application_repository = loan_application_repository

        self.__bank_credit_score_service = bank_credit_score_service
        self.__bank_criminal_record_service = bank_criminal_record_service

    def execute(self, request: "LoanApplicationRequest") -> "LoanApplicationResponse":
        application = LoanApplication(request.ssn, request.amount)

        bank_employee = BankApprover()
        bank_employee.add_approval_criteria(
            [
                IsCreditScoreAcceptable(self.__bank_credit_score_service),
                HasNoCriminalRecord(self.__bank_criminal_record_service),
            ]
        )

        bank_employee.review_application(application)

        self.__loan_application_repository.save(application)

        return LoanApplicationResponse(
            ssn=application.ssn,
            amount=application.amount,
            credit_score=application.credit_score,
            status=application.status,
            rejection_reasons=application.rejection_reasons,
        )
