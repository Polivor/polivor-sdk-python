from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.ap_2_import_result_report import Ap2ImportResultReport
  from ..models.mandate import Mandate





T = TypeVar("T", bound="Ap2ImportResult")



@_attrs_define
class Ap2ImportResult:
    """ 
        Attributes:
            mandate (Mandate):
            report (Ap2ImportResultReport):
     """

    mandate: Mandate
    report: Ap2ImportResultReport
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ap_2_import_result_report import Ap2ImportResultReport # noqa: PLC0415
        from ..models.mandate import Mandate # noqa: PLC0415
        mandate = self.mandate.to_dict()

        report = self.report.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "mandate": mandate,
            "report": report,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ap_2_import_result_report import Ap2ImportResultReport # noqa: PLC0415
        from ..models.mandate import Mandate # noqa: PLC0415
        d = dict(src_dict)
        mandate = Mandate.from_dict(d.pop("mandate"))




        report = Ap2ImportResultReport.from_dict(d.pop("report"))




        ap_2_import_result = cls(
            mandate=mandate,
            report=report,
        )


        ap_2_import_result.additional_properties = d
        return ap_2_import_result

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
