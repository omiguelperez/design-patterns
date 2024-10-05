from acme.domain.entities import LoanApplication
from acme.domain.services.criminal_record import (
    IInternationalCriminalRecordService,
    INationalCriminalRecordService,
)


class MockNationalCriminalRecordService(INationalCriminalRecordService):
    def has_criminal_record(self, application: LoanApplication) -> bool:
        return False


class MockInternationalCriminalRecordService(IInternationalCriminalRecordService):
    def has_criminal_record(self, application: LoanApplication) -> bool:
        return False
