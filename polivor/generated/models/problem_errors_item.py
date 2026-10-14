from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ProblemErrorsItem")



@_attrs_define
class ProblemErrorsItem:
    """ 
        Attributes:
            path (str): JSON Pointer to the offending field
            message (str):
            line (int | Unset): 1-based line when the error points into a text such as a Cedar policy
            column (int | Unset):
     """

    path: str
    message: str
    line: int | Unset = UNSET
    column: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        path = self.path

        message = self.message

        line = self.line

        column = self.column


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "path": path,
            "message": message,
        })
        if line is not UNSET:
            field_dict["line"] = line
        if column is not UNSET:
            field_dict["column"] = column

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path")

        message = d.pop("message")

        line = d.pop("line", UNSET)

        column = d.pop("column", UNSET)

        problem_errors_item = cls(
            path=path,
            message=message,
            line=line,
            column=column,
        )


        problem_errors_item.additional_properties = d
        return problem_errors_item

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
