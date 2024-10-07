from acme.domain.contracts.services import (
    IInternationalCriminalRecordService,
    INationalCriminalRecordService,
)
from acme.domain.entities.application import Application


class BankCriminalRecordService:
    def __init__(
        self,
        national_criminal_record_service: "INationalCriminalRecordService",
        international_criminal_record_service: "IInternationalCriminalRecordService",
    ):
        self.__national_criminal_record_service = national_criminal_record_service
        self.__international_criminal_record_service = international_criminal_record_service

    def has_criminal_record(self, application: "Application") -> bool:
        criminal_record_services = [
            self.__national_criminal_record_service,
            self.__international_criminal_record_service,
        ]
        return any(service.has_criminal_record(application) for service in criminal_record_services)
