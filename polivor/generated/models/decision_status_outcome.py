from enum import StrEnum

class DecisionStatusOutcome(StrEnum):
    ALLOW = "ALLOW"
    DENY = "DENY"
    REQUIRE_APPROVAL = "REQUIRE_APPROVAL"

    def __str__(self) -> str:
        return str(self.value)
