from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.beneficiary_update_status import BeneficiaryUpdateStatus
from ..types import UNSET, Unset






T = TypeVar("T", bound="BeneficiaryUpdate")



@_attrs_define
class BeneficiaryUpdate:
    """ 
        Attributes:
            name (str | Unset):
            iban (str | Unset):
            country (str | Unset):
            status (BeneficiaryUpdateStatus | Unset):
     """

    name: str | Unset = UNSET
    iban: str | Unset = UNSET
    country: str | Unset = UNSET
    status: BeneficiaryUpdateStatus | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        iban = self.iban

        country = self.country

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if iban is not UNSET:
            field_dict["iban"] = iban
        if country is not UNSET:
            field_dict["country"] = country
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        iban = d.pop("iban", UNSET)

        country = d.pop("country", UNSET)

        _status = d.pop("status", UNSET)
        status: BeneficiaryUpdateStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = BeneficiaryUpdateStatus(_status)




        beneficiary_update = cls(
            name=name,
            iban=iban,
            country=country,
            status=status,
        )

        return beneficiary_update

