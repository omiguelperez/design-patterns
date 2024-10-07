from acme.domain.contracts.services import (
    IInternationalCriminalRecordService,
    INationalCriminalRecordService,
)
from acme.domain.entities.application import Application


class MockNationalCriminalRecordService(INationalCriminalRecordService):
    def has_criminal_record(self, application: Application) -> bool:
        return False


class MockInternationalCriminalRecordService(IInternationalCriminalRecordService):
    def has_criminal_record(self, application: Application) -> bool:
        return False
