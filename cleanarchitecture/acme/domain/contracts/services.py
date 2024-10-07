from abc import ABC, abstractmethod

from acme.domain.entities.application import Application


class ICreditScoreService(ABC):
    @abstractmethod
    def get_credit_score(self, application: "Application") -> int:
        raise NotImplementedError


class IExperianCreditScoreService(ICreditScoreService):
    pass


class ITransUnionCreditScoreService(ICreditScoreService):
    pass


class IEquifaxCreditScoreService(ICreditScoreService):
    pass


class ICriminalRecordService(ABC):
    @abstractmethod
    def has_criminal_record(self, application: "Application") -> bool:
        raise NotImplementedError


class INationalCriminalRecordService(ICriminalRecordService):
    pass


class IInternationalCriminalRecordService(ICriminalRecordService):
    pass
