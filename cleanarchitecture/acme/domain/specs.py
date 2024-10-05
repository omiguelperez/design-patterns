from abc import ABC, abstractmethod

from acme.domain.entities.application import Application
from acme.domain.services.credit_score import BankCreditScoreService
from acme.domain.services.criminal_record import BankCriminalRecordService


class Specification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: "Application") -> bool:
        pass


class IsCreditScoreAcceptable(Specification):
    GOOD_CREDIT_SCORE_THRESHOLD = 700

    def __init__(self, bank_credit_score_service: "BankCreditScoreService"):
        self.__bank_credit_score_service = bank_credit_score_service

    def is_satisfied_by(self, application: "Application") -> bool:
        application.credit_score = (
            self.__bank_credit_score_service.get_application_credit_score(application)
        )
        return application.credit_score >= self.GOOD_CREDIT_SCORE_THRESHOLD


class HasNoCriminalRecord(Specification):
    def __init__(self, bank_criminal_record_service: "BankCriminalRecordService"):
        self.__bank_criminal_record_service = bank_criminal_record_service

    def is_satisfied_by(self, application: "Application") -> bool:
        return not self.__bank_criminal_record_service.has_criminal_record(application)
