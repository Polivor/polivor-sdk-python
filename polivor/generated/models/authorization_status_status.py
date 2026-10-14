from enum import StrEnum

class AuthorizationStatusStatus(StrEnum):
    EXECUTED = "EXECUTED"
    FAILED = "FAILED"
    ISSUED = "ISSUED"
    NOT_EXECUTED = "NOT_EXECUTED"
    REJECTED = "REJECTED"

    def __str__(self) -> str:
        return str(self.value)
