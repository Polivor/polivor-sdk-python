from enum import StrEnum

class IdentityProviderStatus(StrEnum):
    ACTIVE = "ACTIVE"
    DISABLED = "DISABLED"

    def __str__(self) -> str:
        return str(self.value)
