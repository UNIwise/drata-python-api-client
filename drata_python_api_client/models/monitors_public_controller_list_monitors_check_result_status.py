from enum import Enum


class MonitorsPublicControllerListMonitorsCheckResultStatus(str, Enum):
    ERROR = "ERROR"
    FAILED = "FAILED"
    PASSED = "PASSED"
    PREAUDIT = "PREAUDIT"
    READY = "READY"

    def __str__(self) -> str:
        return str(self.value)
