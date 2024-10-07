from datetime import datetime

from acme.domain.entities.application import LoanApplication
from acme.domain.repositories import (
    IEligibilityCriteriaRepository,
    ILoanApplicationRepository,
)
from acme.domain.specs import (
    HasNoCriminalRecord,
    HasNotAppliedForCreditCardInTheLast6Months,
    IsCreditScoreAcceptable,
)


class InMemoryLoanApplicationRepository(ILoanApplicationRepository):
    def __init__(self):
        self.__applications = []

    def save(self, application: "LoanApplication"):
        self.__applications.append(application)


class InMemoryCreditCardApplicationRepository(ILoanApplicationRepository):
    def __init__(self):
        self.__applications = []

    def save(self, application: "LoanApplication"):
        self.__applications.append(application)

    def fetch_since_for_applicant(self, since: datetime, applicant_ssn: str):
        return [
            application
            for application in self.__applications
            if application.ssn == applicant_ssn and application.approved_at >= since
        ]


class InMemoryEligibilityCriteriaRepository(IEligibilityCriteriaRepository):
    def __init__(self):
        self.__credit_card_approval_criteria_types = [
            IsCreditScoreAcceptable,
            HasNoCriminalRecord,
            HasNotAppliedForCreditCardInTheLast6Months,
        ]
        self.__loan_approval_criteria_types = [
            IsCreditScoreAcceptable,
            HasNoCriminalRecord,
        ]

    def fetch_credit_card_approval_criteria_types(self):
        return self.__credit_card_approval_criteria_types

    def fetch_loan_approval_criteria_types(self):
        return self.__loan_approval_criteria_types
