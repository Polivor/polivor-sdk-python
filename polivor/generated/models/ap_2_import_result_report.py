from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="Ap2ImportResultReport")



@_attrs_define
class Ap2ImportResultReport:
    """ 
        Attributes:
            mapped (list[str]): Native fields filled from the credential
            unmapped (list[str]): Parts of the credential that a native mandate does not enforce
            missing (list[str]): Native fields still to be completed before activation
     """

    mapped: list[str]
    unmapped: list[str]
    missing: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        mapped = self.mapped



        unmapped = self.unmapped



        missing = self.missing




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "mapped": mapped,
            "unmapped": unmapped,
            "missing": missing,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mapped = cast(list[str], d.pop("mapped"))


        unmapped = cast(list[str], d.pop("unmapped"))


        missing = cast(list[str], d.pop("missing"))


        ap_2_import_result_report = cls(
            mapped=mapped,
            unmapped=unmapped,
            missing=missing,
        )


        ap_2_import_result_report.additional_properties = d
        return ap_2_import_result_report

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
