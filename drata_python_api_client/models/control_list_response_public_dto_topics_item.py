from enum import Enum


class ControlListResponsePublicDtoTopicsItem(str, Enum):
    ADMINISTRATIVE_SAFEGUARDS = "ADMINISTRATIVE_SAFEGUARDS"
    AVAILABILITY = "AVAILABILITY"
    BASIC = "BASIC"
    CONFIDENTIALITY = "CONFIDENTIALITY"
    DERIVED = "DERIVED"
    GENERAL_RULES = "GENERAL_RULES"
    NIST80053_PRIVACY = "NIST80053_PRIVACY"
    PHYSICAL_SAFEGUARDS = "PHYSICAL_SAFEGUARDS"
    PRIVACY = "PRIVACY"
    PROCESS_INTEGRITY = "PROCESS_INTEGRITY"
    REQUIREMENTS_ORGANIZATION = "REQUIREMENTS_ORGANIZATION"
    REQUIREMENTS_POLICIES_PROCEDURES = "REQUIREMENTS_POLICIES_PROCEDURES"
    SECURITY = "SECURITY"
    TECHNICAL_SAFEGUARDS = "TECHNICAL_SAFEGUARDS"

    def __str__(self) -> str:
        return str(self.value)
