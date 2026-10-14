from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.action_payment_type import ActionPaymentType
from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.beneficiary_ref import BeneficiaryRef





T = TypeVar("T", bound="Action")



@_attrs_define
class Action:
    """ Unknown fields are ignored and never influence the decision.

        Attributes:
            type_ (Literal['PayInvoice']):
            amount_minor (int): Integer minor units (cents); never a float
            currency (str):
            debtor_account (str):
            payment_type (ActionPaymentType):
            beneficiary (BeneficiaryRef): Unknown fields are ignored. Everything decisive about the beneficiary is computed
                by Polivor from the allowlist and the IBAN.
            reference (str):
     """

    type_: Literal['PayInvoice']
    amount_minor: int
    currency: str
    debtor_account: str
    payment_type: ActionPaymentType
    beneficiary: BeneficiaryRef
    reference: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.beneficiary_ref import BeneficiaryRef # noqa: PLC0415
        type_ = self.type_

        amount_minor = self.amount_minor

        currency = self.currency

        debtor_account = self.debtor_account

        payment_type = self.payment_type.value

        beneficiary = self.beneficiary.to_dict()

        reference = self.reference


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
            "amount_minor": amount_minor,
            "currency": currency,
            "debtor_account": debtor_account,
            "payment_type": payment_type,
            "beneficiary": beneficiary,
            "reference": reference,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.beneficiary_ref import BeneficiaryRef # noqa: PLC0415
        d = dict(src_dict)
        type_ = cast(Literal['PayInvoice'] , d.pop("type"))
        if type_ != 'PayInvoice':
            raise ValueError(f"type must match const 'PayInvoice', got '{type_}'")

        amount_minor = d.pop("amount_minor")

        currency = d.pop("currency")

        debtor_account = d.pop("debtor_account")

        payment_type = ActionPaymentType(d.pop("payment_type"))




        beneficiary = BeneficiaryRef.from_dict(d.pop("beneficiary"))




        reference = d.pop("reference")

        action = cls(
            type_=type_,
            amount_minor=amount_minor,
            currency=currency,
            debtor_account=debtor_account,
            payment_type=payment_type,
            beneficiary=beneficiary,
            reference=reference,
        )


        action.additional_properties = d
        return action

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
