from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.beneficiary_create_status import BeneficiaryCreateStatus
from ..types import UNSET, Unset






T = TypeVar("T", bound="BeneficiaryCreate")



@_attrs_define
class BeneficiaryCreate:
    """ 
        Attributes:
            external_id (str): The ID the agent sends in an authorize request; letters, digits and . _ : @ / -
            name (str):
            iban (str): Spaces and lowercase are accepted and normalised; the checksum is verified
            country (str):
            status (BeneficiaryCreateStatus | Unset):  Default: BeneficiaryCreateStatus.APPROVED.
     """

    external_id: str
    name: str
    iban: str
    country: str
    status: BeneficiaryCreateStatus | Unset = BeneficiaryCreateStatus.APPROVED





    def to_dict(self) -> dict[str, Any]:
        external_id = self.external_id

        name = self.name

        iban = self.iban

        country = self.country

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
            "external_id": external_id,
            "name": name,
            "iban": iban,
            "country": country,
        })
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        external_id = d.pop("external_id")

        name = d.pop("name")

        iban = d.pop("iban")

        country = d.pop("country")

        _status = d.pop("status", UNSET)
        status: BeneficiaryCreateStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = BeneficiaryCreateStatus(_status)




        beneficiary_create = cls(
            external_id=external_id,
            name=name,
            iban=iban,
            country=country,
            status=status,
        )

        return beneficiary_create

