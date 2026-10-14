from enum import StrEnum

class DecisionStatusStatus(StrEnum):
    ALLOWED = "ALLOWED"
    DENIED = "DENIED"
    PENDING_APPROVAL = "PENDING_APPROVAL"

    def __str__(self) -> str:
        return str(self.value)
