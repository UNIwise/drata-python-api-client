from enum import Enum


class GRCPublicControllerGetControlsSubRulesItem(str, Enum):
    ADMINISTRATIVE_SAFEGUARDS = "ADMINISTRATIVE_SAFEGUARDS"
    GENERAL_RULES = "GENERAL_RULES"
    PHYSICAL_SAFEGUARDS = "PHYSICAL_SAFEGUARDS"
    REQUIREMENTS_ORGANIZATION = "REQUIREMENTS_ORGANIZATION"
    REQUIREMENTS_POLICIES_PROCEDURES = "REQUIREMENTS_POLICIES_PROCEDURES"
    TECHNICAL_SAFEGUARDS = "TECHNICAL_SAFEGUARDS"

    def __str__(self) -> str:
        return str(self.value)
