from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="BeneficiaryRef")



@_attrs_define
class BeneficiaryRef:
    """ Unknown fields are ignored. Everything decisive about the beneficiary is computed by Polivor from the allowlist and
    the IBAN.

        Attributes:
            id (str):
            iban (str):
            country (str | Unset): Accepted for compatibility and never used
     """

    id: str
    iban: str
    country: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        iban = self.iban

        country = self.country


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "iban": iban,
        })
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        iban = d.pop("iban")

        country = d.pop("country", UNSET)

        beneficiary_ref = cls(
            id=id,
            iban=iban,
            country=country,
        )


        beneficiary_ref.additional_properties = d
        return beneficiary_ref

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
