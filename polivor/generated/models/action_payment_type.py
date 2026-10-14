from enum import StrEnum

class ActionPaymentType(StrEnum):
    SEPA_CT = "SEPA_CT"
    SEPA_INST = "SEPA_INST"

    def __str__(self) -> str:
        return str(self.value)
