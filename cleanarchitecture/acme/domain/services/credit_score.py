from abc import ABC, abstractmethod

from acme.domain.entities import LoanApplication


class ICreditScoreService(ABC):
    @abstractmethod
    def get_credit_score(self, application: "LoanApplication") -> int:
        raise NotImplementedError


class IExperianCreditScoreService(ICreditScoreService):
    pass


class ITransUnionCreditScoreService(ICreditScoreService):
    pass


class IEquifaxCreditScoreService(ICreditScoreService):
    pass


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
