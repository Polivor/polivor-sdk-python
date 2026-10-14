from enum import StrEnum

class CheckResult(StrEnum):
    FAIL = "fail"
    NOT_SATISFIED = "not_satisfied"
    PASS = "pass"
    SATISFIED = "satisfied"

    def __str__(self) -> str:
        return str(self.value)
