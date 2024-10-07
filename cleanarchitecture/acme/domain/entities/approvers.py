from abc import ABC

from acme.domain.entities.application import Application
from acme.domain.specs import EligibilityCriterion


class BankEmployee(ABC):
    pass


class BankApprover(BankEmployee):
    def __init__(self):
        self.__bank_approval_criteria = []

    def add_approval_criteria(self, approval_criteria: list["EligibilityCriterion"]):
        self.__bank_approval_criteria.extend(approval_criteria)

    def review_application(self, application: "Application"):
        failed_criteria = [
            criteria
            for criteria in self.__bank_approval_criteria
            if not criteria.is_satisfied_by(application)
        ]

        if any(failed_criteria):
            reasons = [criteria.fail_reason for criteria in failed_criteria]
            application.reject(reasons)
        else:
            application.approve()
