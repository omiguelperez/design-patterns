from acme.domain.entities.application import Application
from acme.domain.services.criminal_record import (
    IInternationalCriminalRecordService,
    INationalCriminalRecordService,
)


class MockNationalCriminalRecordService(INationalCriminalRecordService):
    def has_criminal_record(self, application: Application) -> bool:
        return False


class MockInternationalCriminalRecordService(IInternationalCriminalRecordService):
    def has_criminal_record(self, application: Application) -> bool:
        return False
