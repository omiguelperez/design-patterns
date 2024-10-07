from typing import Callable, Dict, Type

from acme.domain.exceptions import SpecificationTypeNotFound
from acme.domain.repositories import ICreditCardApplicationRepository
from acme.domain.services.credit_score import BankCreditScoreService
from acme.domain.services.criminal_record import BankCriminalRecordService
from acme.domain.specs import (
    EligibilityCriterion,
    HasNoCriminalRecord,
    HasNotAppliedForCreditCardInTheLast6Months,
    IsCreditScoreAcceptable,
)


class EligibilityCriteriaFactory:
    def __init__(
        self,
        bank_credit_score_service: "BankCreditScoreService",
        bank_criminal_record_service: "BankCriminalRecordService",
        credit_card_application_repository: "ICreditCardApplicationRepository",
    ) -> None:
        self.__specification_map: Dict[str, Callable[[], EligibilityCriterion]] = {
            IsCreditScoreAcceptable: lambda: IsCreditScoreAcceptable(bank_credit_score_service),
            HasNoCriminalRecord: lambda: HasNoCriminalRecord(bank_criminal_record_service),
            HasNotAppliedForCreditCardInTheLast6Months: lambda: HasNotAppliedForCreditCardInTheLast6Months(
                credit_card_application_repository
            ),
        }

    def create_many(self, spec_types: list[str]) -> EligibilityCriterion:
        return [self.create(spec_type) for spec_type in spec_types]

    def create(self, spec_type: str) -> Type[EligibilityCriterion]:
        try:
            return self.__specification_map[spec_type]()
        except KeyError:
            raise SpecificationTypeNotFound(spec_type)
