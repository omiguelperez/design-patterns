from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional

from pydantic import BaseModel

# Domain


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


class BankFinancialEmployee:
    def __init__(self):
        self.__bank_criminal_record_service: BankCriminalRecordService = None
        self.__bank_credit_score_service: BankCreditScoreService = None

    def use_criminal_record_service(self, service: "BankCriminalRecordService"):
        self.__bank_criminal_record_service = service

    def use_credit_score_service(self, service: "BankCreditScoreService"):
        self.__bank_credit_score_service = service

    def apply_loan(self, application: "LoanApplication"):
        if self.__has_good_credit_score(application) and not self.__has_criminal_record(
            application
        ):
            application.approve()
        else:
            application.reject()

    def __has_good_credit_score(self, application: "LoanApplication") -> bool:
        application.credit_score = (
            self.__bank_credit_score_service.get_application_credit_score(application)
        )
        return application.credit_score > 700

    def __has_criminal_record(self, application: "LoanApplication") -> bool:
        return self.__bank_criminal_record_service.has_criminal_record(application)


class ICreditScoreService(ABC):
    @abstractmethod
    def get_credit_score(self, application: LoanApplication) -> int:
        raise NotImplementedError


class IExperianCreditScoreService(ICreditScoreService):
    pass


class ITransUnionCreditScoreService(ICreditScoreService):
    pass


class IEquifaxCreditScoreService(ICreditScoreService):
    pass


class ILoanApplicationRepository(ABC):
    @abstractmethod
    def save(self, application: LoanApplication):
        raise NotImplementedError


class ICriminalRecordService(ABC):
    @abstractmethod
    def has_criminal_record(self, application: LoanApplication) -> bool:
        raise NotImplementedError


class INationalCriminalRecordService(ICriminalRecordService):
    def has_criminal_record(self, application: LoanApplication) -> bool:
        raise NotImplementedError


class IInternationalCriminalRecordService(ICriminalRecordService):
    def has_criminal_record(self, application: LoanApplication) -> bool:
        raise NotImplementedError


class BankCreditScoreService:
    def __init__(
        self,
        experian_credit_score_service: IExperianCreditScoreService,
        trans_union_credit_score_service: ITransUnionCreditScoreService,
        equifax_credit_score_service: IEquifaxCreditScoreService,
    ):
        self.__experian_credit_score_service = experian_credit_score_service
        self.__trans_union_credit_score_service = trans_union_credit_score_service
        self.__equifax_credit_score = equifax_credit_score_service

    def get_application_credit_score(self, application: LoanApplication) -> int:
        credit_score_services = [
            self.__experian_credit_score_service,
            self.__trans_union_credit_score_service,
            self.__equifax_credit_score,
        ]
        credit_scores = [
            service.get_credit_score(application) for service in credit_score_services
        ]
        return sum(credit_scores) // len(credit_scores)


class BankCriminalRecordService:
    def __init__(
        self,
        national_criminal_record_service: "INationalCriminalRecordService",
        international_criminal_record_service: "IInternationalCriminalRecordService",
    ):
        self.__national_criminal_record_service = national_criminal_record_service
        self.__international_criminal_record_service = (
            international_criminal_record_service
        )

    def has_criminal_record(self, application: LoanApplication) -> bool:
        criminal_record_services = [
            self.__national_criminal_record_service,
            self.__international_criminal_record_service,
        ]
        return any(
            service.has_criminal_record(application)
            for service in criminal_record_services
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
        bank_employee.use_criminal_record_service(self.__bank_criminal_record_service)
        bank_employee.use_credit_score_service(self.__bank_credit_score_service)

        bank_employee.apply_loan(application)

        self.__loan_application_repository.save(application)

        return LoanApplicationResponse(
            name=application.name,
            amount=application.amount,
            credit_score=application.credit_score,
            status=application.status,
        )


# Infrastructure - Repositories


class InMemoryLoanApplicationRepository(ILoanApplicationRepository):
    def __init__(self):
        self.__applications = []

    def save(self, application: LoanApplication):
        self.__applications.append(application)


# Infrastructure - Services


class MockExperianCreditScoreService(IExperianCreditScoreService):
    def get_credit_score(self, application: LoanApplication) -> int:
        return 700


class MockTransUnionCreditScoreService(ITransUnionCreditScoreService):
    def get_credit_score(self, application: LoanApplication) -> int:
        return 720


class MockEquifaxCreditScoreService(IEquifaxCreditScoreService):
    def get_credit_score(self, application: LoanApplication) -> int:
        return 680


class MockNationalCriminalRecordService(INationalCriminalRecordService):
    def has_criminal_record(self, application: LoanApplication) -> bool:
        return False


class MockInternationalCriminalRecordService(IInternationalCriminalRecordService):
    def has_criminal_record(self, application: LoanApplication) -> bool:
        return False


# Application

from dependency_injector import containers, providers


class LoanContainer(containers.DeclarativeContainer):
    loan_application_repository = providers.Singleton(InMemoryLoanApplicationRepository)
    experian_credit_score_service = providers.Singleton(MockExperianCreditScoreService)
    trans_union_credit_score_service = providers.Singleton(
        MockTransUnionCreditScoreService
    )
    equifax_credit_score_service = providers.Singleton(MockEquifaxCreditScoreService)
    national_criminal_record_service = providers.Singleton(
        MockNationalCriminalRecordService
    )
    international_criminal_record_service = providers.Singleton(
        MockInternationalCriminalRecordService
    )
    bank_credit_score_service = providers.Factory(
        BankCreditScoreService,
        experian_credit_score_service=experian_credit_score_service.provided,
        trans_union_credit_score_service=trans_union_credit_score_service.provided,
        equifax_credit_score_service=equifax_credit_score_service.provided,
    )
    bank_criminal_record_service = providers.Factory(
        BankCriminalRecordService,
        national_criminal_record_service=national_criminal_record_service.provided,
        international_criminal_record_service=international_criminal_record_service.provided,
    )
    loan_apply_use_case = providers.Factory(
        LoanApplyUseCase,
        loan_application_repository=loan_application_repository.provided,
        bank_credit_score_service=bank_credit_score_service.provided,
        bank_criminal_record_service=bank_criminal_record_service.provided,
    )


# Infrastructure - API


def apply():
    loan_apply_use_case = LoanContainer.loan_apply_use_case()
    request = LoanApplicationRequest(name="John Doe", amount=1000)
    response = loan_apply_use_case.execute(request)
    print(response)


if __name__ == "__main__":
    apply()
