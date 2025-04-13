from enum import Enum


class DevicePublicControllerGetDevicesForCustomConnectionExpandItem(str, Enum):
    ASSET = "ASSET"
    COMPLIANCE_CHECKS = "COMPLIANCE_CHECKS"
    DOCUMENTS = "DOCUMENTS"
    IDENTIFIERS = "IDENTIFIERS"

    def __str__(self) -> str:
        return str(self.value)
