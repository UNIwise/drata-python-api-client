from enum import Enum


class GRCPublicControllerGetControlsDrataFunctionsItem(str, Enum):
    DRATA_ESSENTIALS_DETECT = "DRATA_ESSENTIALS_DETECT"
    DRATA_ESSENTIALS_GOVERN = "DRATA_ESSENTIALS_GOVERN"
    DRATA_ESSENTIALS_IDENTIFY = "DRATA_ESSENTIALS_IDENTIFY"
    DRATA_ESSENTIALS_PROTECT = "DRATA_ESSENTIALS_PROTECT"
    DRATA_ESSENTIALS_RECOVER = "DRATA_ESSENTIALS_RECOVER"
    DRATA_ESSENTIALS_RESPOND = "DRATA_ESSENTIALS_RESPOND"

    def __str__(self) -> str:
        return str(self.value)
