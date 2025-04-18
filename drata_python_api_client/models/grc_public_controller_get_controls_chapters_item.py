from enum import Enum


class GRCPublicControllerGetControlsChaptersItem(str, Enum):
    GDPR_CONTROLLER_AND_PROCESSOR = "GDPR_CONTROLLER_AND_PROCESSOR"
    GDPR_PRINCIPLES = "GDPR_PRINCIPLES"
    GDPR_RIGHTS_OF_THE_DATA_SUBJECT = "GDPR_RIGHTS_OF_THE_DATA_SUBJECT"
    GDPR_TRANSFERS_OF_PERSONNEL_DATA_TO_THIRD_COUNTRIES_OR_INTERNATIONAL_ORGANIZATIONS = (
        "GDPR_TRANSFERS_OF_PERSONNEL_DATA_TO_THIRD_COUNTRIES_OR_INTERNATIONAL_ORGANIZATIONS"
    )

    def __str__(self) -> str:
        return str(self.value)
