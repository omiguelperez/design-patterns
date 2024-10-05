from typing import Optional

from pydantic import BaseModel

from acme.domain.entities import (
    BankFinancialEmployee,
    LoanApplication,
    LoanApplicationStatus,
)
from acme.domain.repositories import ILoanApplicationRepository
from acme.domain.services.credit_score import BankCreditScoreService
from acme.domain.services.criminal_record import BankCriminalRecordService
from acme.domain.specs.loan_application import (
    HasNoCriminalRecord,
    IsCreditScoreAcceptable,
)


class LoanApplicationRequest(BaseModel):
    name: str
    amount: float


class LoanApplicationResponse(BaseModel):
    name: str
    amount: float
    credit_score: Optional[int]
    status: LoanApplicationStatus


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
        application = LoanApplication(request.name, request.amount)

        bank_employee = BankFinancialEmployee()
        bank_employee.let_him_know_requirements_to_approve_loan(
            IsCreditScoreAcceptable(self.__bank_credit_score_service),
            HasNoCriminalRecord(self.__bank_criminal_record_service),
        )

        bank_employee.apply_loan(application)

        self.__loan_application_repository.save(application)

        return LoanApplicationResponse(
            name=application.name,
            amount=application.amount,
            credit_score=application.credit_score,
            status=application.status,
        )
