from enum import StrEnum

class JwkUse(StrEnum):
    AUTHZ = "authz"
    EVIDENCE = "evidence"

    def __str__(self) -> str:
        return str(self.value)
