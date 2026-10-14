from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.execution_report_status import ExecutionReportStatus
from ..types import UNSET, Unset






T = TypeVar("T", bound="ExecutionReport")



@_attrs_define
class ExecutionReport:
    """ 
        Attributes:
            status (ExecutionReportStatus):
            external_ref (str | Unset):
     """

    status: ExecutionReportStatus
    external_ref: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        external_ref = self.external_ref


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "status": status,
        })
        if external_ref is not UNSET:
            field_dict["external_ref"] = external_ref

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = ExecutionReportStatus(d.pop("status"))




        external_ref = d.pop("external_ref", UNSET)

        execution_report = cls(
            status=status,
            external_ref=external_ref,
        )

        return execution_report

