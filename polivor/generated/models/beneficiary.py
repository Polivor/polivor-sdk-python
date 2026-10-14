from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.beneficiary_status import BeneficiaryStatus
from uuid import UUID






T = TypeVar("T", bound="Beneficiary")



@_attrs_define
class Beneficiary:
    """ 
        Attributes:
            id (UUID):
            external_id (str):
            name (str):
            iban (str):
            country (str):
            status (BeneficiaryStatus):
     """

    id: UUID
    external_id: str
    name: str
    iban: str
    country: str
    status: BeneficiaryStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        external_id = self.external_id

        name = self.name

        iban = self.iban

        country = self.country

        status = self.status.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "external_id": external_id,
            "name": name,
            "iban": iban,
            "country": country,
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        external_id = d.pop("external_id")

        name = d.pop("name")

        iban = d.pop("iban")

        country = d.pop("country")

        status = BeneficiaryStatus(d.pop("status"))




        beneficiary = cls(
            id=id,
            external_id=external_id,
            name=name,
            iban=iban,
            country=country,
            status=status,
        )


        beneficiary.additional_properties = d
        return beneficiary

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
