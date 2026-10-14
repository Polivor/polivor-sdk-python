from enum import StrEnum

class MandateStatus(StrEnum):
    ACTIVE = "ACTIVE"
    DRAFT = "DRAFT"
    REVOKED = "REVOKED"
    SUSPENDED = "SUSPENDED"

    def __str__(self) -> str:
        return str(self.value)
