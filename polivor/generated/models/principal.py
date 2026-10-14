from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="Principal")



@_attrs_define
class Principal:
    """ 
        Attributes:
            id (UUID):
            legal_name (str):
            country (str):
            lei (str | Unset):
     """

    id: UUID
    legal_name: str
    country: str
    lei: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        legal_name = self.legal_name

        country = self.country

        lei = self.lei


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "legal_name": legal_name,
            "country": country,
        })
        if lei is not UNSET:
            field_dict["lei"] = lei

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        legal_name = d.pop("legal_name")

        country = d.pop("country")

        lei = d.pop("lei", UNSET)

        principal = cls(
            id=id,
            legal_name=legal_name,
            country=country,
            lei=lei,
        )


        principal.additional_properties = d
        return principal

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
