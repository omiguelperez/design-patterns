from abc import ABC

from acme.domain.entities.application import Application
from acme.domain.specs import Specification


class BankEmployee(ABC):
    pass


class BankApprover(BankEmployee):
    def __init__(self):
        self.__bank_requirements_to_approve_application = []

    def let_him_know_requirements_to_approve_application(
        self, *requirements: list["Specification"]
    ):
        self.__bank_requirements_to_approve_application.extend(requirements)

    def review_application(self, application: "Application"):
        all_requirements_met = all(
            requirement.is_satisfied_by(application)
            for requirement in self.__bank_requirements_to_approve_application
        )
        if all_requirements_met:
            application.approve()
        else:
            application.reject()
