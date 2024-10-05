from acme.domain.entities import LoanApplication
from acme.domain.services.credit_score import (
    IEquifaxCreditScoreService,
    IExperianCreditScoreService,
    ITransUnionCreditScoreService,
)


class MockExperianCreditScoreService(IExperianCreditScoreService):
    def get_credit_score(self, application: LoanApplication) -> int:
        return 700


class MockTransUnionCreditScoreService(ITransUnionCreditScoreService):
    def get_credit_score(self, application: LoanApplication) -> int:
        return 720


class MockEquifaxCreditScoreService(IEquifaxCreditScoreService):
    def get_credit_score(self, application: LoanApplication) -> int:
        return 680
