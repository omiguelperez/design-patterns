from acme.domain.entities.application import Application
from acme.domain.services.credit_score import (
    IEquifaxCreditScoreService,
    IExperianCreditScoreService,
    ITransUnionCreditScoreService,
)


class MockExperianCreditScoreService(IExperianCreditScoreService):
    def get_credit_score(self, application: Application) -> int:
        return 700


class MockTransUnionCreditScoreService(ITransUnionCreditScoreService):
    def get_credit_score(self, application: Application) -> int:
        return 720


class MockEquifaxCreditScoreService(IEquifaxCreditScoreService):
    def get_credit_score(self, application: Application) -> int:
        return 680
