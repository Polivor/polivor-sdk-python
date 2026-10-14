from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Signals")



@_attrs_define
class Signals:
    """ Agent-supplied; may only be used in forbid rules (signals tighten, never loosen). Unknown fields are ignored.

        Attributes:
            origin (str | Unset):
            risk_flags (list[str] | Unset):
     """

    origin: str | Unset = UNSET
    risk_flags: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        origin = self.origin

        risk_flags: list[str] | Unset = UNSET
        if not isinstance(self.risk_flags, Unset):
            risk_flags = self.risk_flags




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if origin is not UNSET:
            field_dict["origin"] = origin
        if risk_flags is not UNSET:
            field_dict["risk_flags"] = risk_flags

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        origin = d.pop("origin", UNSET)

        risk_flags = cast(list[str], d.pop("risk_flags", UNSET))


        signals = cls(
            origin=origin,
            risk_flags=risk_flags,
        )


        signals.additional_properties = d
        return signals

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
