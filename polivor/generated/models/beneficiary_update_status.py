from enum import StrEnum

class BeneficiaryUpdateStatus(StrEnum):
    APPROVED = "APPROVED"
    BLOCKED = "BLOCKED"

    def __str__(self) -> str:
        return str(self.value)
