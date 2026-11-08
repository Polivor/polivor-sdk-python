from enum import StrEnum

class IdentityProviderStatus(StrEnum):
    ACTIVE = "ACTIVE"
    DISABLED = "DISABLED"
    PENDING = "PENDING"

    def __str__(self) -> str:
        return str(self.value)
