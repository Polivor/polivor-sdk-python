from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.denial_code import DenialCode






T = TypeVar("T", bound="Denial")



@_attrs_define
class Denial:
    """ What an agent is told when nothing was allowed (ADR-025). The list of codes is closed and each sentence says what to
    do, never why.
    `retryable` is true only when sending the same request again later, with nothing else changed, may succeed
    (UNAVAILABLE).

        Attributes:
            code (DenialCode):
            message (str):
            retryable (bool):
     """

    code: DenialCode
    message: str
    retryable: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        code = self.code.value

        message = self.message

        retryable = self.retryable


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "code": code,
            "message": message,
            "retryable": retryable,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = DenialCode(d.pop("code"))




        message = d.pop("message")

        retryable = d.pop("retryable")

        denial = cls(
            code=code,
            message=message,
            retryable=retryable,
        )


        denial.additional_properties = d
        return denial

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
