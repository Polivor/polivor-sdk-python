from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Literal, cast






T = TypeVar("T", bound="MandateBody")



@_attrs_define
class MandateBody:
    """ Native Financial Mandate body. The authoritative definition is docs/schema/financial-mandate.v0.json; validated
    against it on write. A DRAFT imported from AP2 holds only the mapped fields until a complete version is added.

        Attributes:
            schema (Literal['polivor.financial-mandate/v0']):
     """

    schema: Literal['polivor.financial-mandate/v0']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        schema = self.schema


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "schema": schema,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        schema = cast(Literal['polivor.financial-mandate/v0'] , d.pop("schema"))
        if schema != 'polivor.financial-mandate/v0':
            raise ValueError(f"schema must match const 'polivor.financial-mandate/v0', got '{schema}'")

        mandate_body = cls(
            schema=schema,
        )


        mandate_body.additional_properties = d
        return mandate_body

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
