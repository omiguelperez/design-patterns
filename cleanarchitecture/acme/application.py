from acme.domain.services.credit_score import BankCreditScoreService
from acme.domain.services.criminal_record import BankCriminalRecordService
from acme.domain.usecases.apply_credit_card import CreditCardApplyUseCase
from acme.domain.usecases.apply_loan import LoanApplyUseCase
from acme.infrastructure.repositories import (
    InMemoryCreditCardApplicationRepository,
    InMemoryLoanApplicationRepository,
)
from acme.infrastructure.services.credit_score import (
    MockEquifaxCreditScoreService,
    MockExperianCreditScoreService,
    MockTransUnionCreditScoreService,
)
from acme.infrastructure.services.criminal_record import (
    MockInternationalCriminalRecordService,
    MockNationalCriminalRecordService,
)
from dependency_injector import containers, providers


class LoanContainer(containers.DeclarativeContainer):
    loan_application_repository = providers.Singleton(InMemoryLoanApplicationRepository)
    credit_card_application_repository = providers.Singleton(
        InMemoryCreditCardApplicationRepository
    )
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
    credit_card_apply_use_case = providers.Factory(
        CreditCardApplyUseCase,
        credit_card_application_repository=credit_card_application_repository.provided,
        bank_credit_score_service=bank_credit_score_service.provided,
        bank_criminal_record_service=bank_criminal_record_service.provided,
    )
