from abc import ABC, abstractmethod
from datetime import datetime, timedelta

from acme.domain.entities.application import Application
from acme.domain.repositories import ICreditCardApplicationRepository
from acme.domain.services.credit_score import BankCreditScoreService
from acme.domain.services.criminal_record import BankCriminalRecordService


class Specification(ABC):
    fail_reason: str = "Failed to meet certain criteria. No more information available."

    @abstractmethod
    def is_satisfied_by(self, candidate: "Application") -> bool:
        pass


class IsCreditScoreAcceptable(Specification):
    GOOD_CREDIT_SCORE_THRESHOLD = 700
    fail_reason = "Credit score is not acceptable."

    def __init__(self, bank_credit_score_service: "BankCreditScoreService"):
        self.__bank_credit_score_service = bank_credit_score_service

    def is_satisfied_by(self, application: "Application") -> bool:
        application.credit_score = (
            self.__bank_credit_score_service.get_application_credit_score(application)
        )
        return application.credit_score >= self.GOOD_CREDIT_SCORE_THRESHOLD


class HasNoCriminalRecord(Specification):
    fail_reason = "Applicant has a criminal record."

    def __init__(self, bank_criminal_record_service: "BankCriminalRecordService"):
        self.__bank_criminal_record_service = bank_criminal_record_service

    def is_satisfied_by(self, application: "Application") -> bool:
        return not self.__bank_criminal_record_service.has_criminal_record(application)


class HasNotAppliedForCreditCardInTheLast6Months(Specification):
    fail_reason = "Applicant has applied for a credit card in the last 6 months."

    def __init__(
        self, credit_card_application_repository: "ICreditCardApplicationRepository"
    ):
        self.__credit_card_application_repository = credit_card_application_repository

    def is_satisfied_by(self, application: "Application") -> bool:
        six_months_ago = datetime.now() - timedelta(days=180)

        applications_in_the_last_6_months = (
            self.__credit_card_application_repository.fetch_since_for_applicant(
                six_months_ago, application.ssn
            )
        )
        return not applications_in_the_last_6_months
