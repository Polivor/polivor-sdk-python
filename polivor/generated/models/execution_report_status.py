from enum import StrEnum

class ExecutionReportStatus(StrEnum):
    EXECUTED = "EXECUTED"
    FAILED = "FAILED"
    REJECTED = "REJECTED"

    def __str__(self) -> str:
        return str(self.value)
