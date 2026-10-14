from enum import StrEnum

class AuthorizeResponseOutcome(StrEnum):
    ALLOW = "ALLOW"
    DENY = "DENY"
    REQUIRE_APPROVAL = "REQUIRE_APPROVAL"

    def __str__(self) -> str:
        return str(self.value)
