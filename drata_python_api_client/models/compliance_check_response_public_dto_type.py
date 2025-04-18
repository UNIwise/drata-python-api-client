from enum import Enum


class ComplianceCheckResponsePublicDtoType(str, Enum):
    ACCEPTED_POLICIES = "ACCEPTED_POLICIES"
    AGENT_INSTALLED = "AGENT_INSTALLED"
    ANTIVIRUS = "ANTIVIRUS"
    AUTO_UPDATES = "AUTO_UPDATES"
    BG_CHECK = "BG_CHECK"
    FULL_COMPLIANCE = "FULL_COMPLIANCE"
    HDD_ENCRYPTION = "HDD_ENCRYPTION"
    HIPAA_TRAINING = "HIPAA_TRAINING"
    IDENTITY_MFA = "IDENTITY_MFA"
    LOCATION_SERVICES = "LOCATION_SERVICES"
    LOCK_SCREEN = "LOCK_SCREEN"
    NIST_AI_TRAINING = "NIST_AI_TRAINING"
    OFFBOARDING = "OFFBOARDING"
    PASSWORD_MANAGER = "PASSWORD_MANAGER"
    SECURITY_TRAINING = "SECURITY_TRAINING"

    def __str__(self) -> str:
        return str(self.value)
