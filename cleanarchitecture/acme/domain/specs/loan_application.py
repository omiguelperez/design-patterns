from abc import ABC, abstractmethod

from acme.domain.entities import LoanApplication
from acme.domain.services.credit_score import BankCreditScoreService
from acme.domain.services.criminal_record import BankCriminalRecordService


class LoanSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: "LoanApplication") -> bool:
        pass


class IsCreditScoreAcceptable(LoanSpecification):
    GOOD_CREDIT_SCORE_THRESHOLD = 700

    def __init__(self, bank_credit_score_service: "BankCreditScoreService"):
        self.__bank_credit_score_service = bank_credit_score_service

    def is_satisfied_by(self, application: "LoanApplication") -> bool:
        application.credit_score = (
            self.__bank_credit_score_service.get_application_credit_score(application)
        )
        return application.credit_score >= self.GOOD_CREDIT_SCORE_THRESHOLD


class HasNoCriminalRecord(LoanSpecification):
    def __init__(self, bank_criminal_record_service: "BankCriminalRecordService"):
        self.__bank_criminal_record_service = bank_criminal_record_service

    def is_satisfied_by(self, application: "LoanApplication") -> bool:
        return not self.__bank_criminal_record_service.has_criminal_record(application)
