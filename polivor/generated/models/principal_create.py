from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PrincipalCreate")



@_attrs_define
class PrincipalCreate:
    """ 
        Attributes:
            legal_name (str):
            country (str):
            lei (str | Unset):
     """

    legal_name: str
    country: str
    lei: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        legal_name = self.legal_name

        country = self.country

        lei = self.lei


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "legal_name": legal_name,
            "country": country,
        })
        if lei is not UNSET:
            field_dict["lei"] = lei

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        legal_name = d.pop("legal_name")

        country = d.pop("country")

        lei = d.pop("lei", UNSET)

        principal_create = cls(
            legal_name=legal_name,
            country=country,
            lei=lei,
        )

        return principal_create

