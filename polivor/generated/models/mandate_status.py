from enum import StrEnum

class MandateStatus(StrEnum):
    ACTIVE = "ACTIVE"
    DRAFT = "DRAFT"
    REVOKED = "REVOKED"

    def __str__(self) -> str:
        return str(self.value)
