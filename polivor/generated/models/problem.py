from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.problem_errors_item import ProblemErrorsItem





T = TypeVar("T", bound="Problem")



@_attrs_define
class Problem:
    """ 
        Attributes:
            type_ (str):
            title (str):
            status (int):
            code (str): Stable machine-readable code. Common ones: UNAUTHENTICATED, FORBIDDEN, NOT_FOUND, MALFORMED_REQUEST,
                VALIDATION_FAILED, RATE_LIMITED,
                IDEMPOTENCY_KEY_REQUIRED, IDEMPOTENCY_KEY_REUSED, IDEMPOTENCY_KEY_EXPIRED, ALREADY_REPORTED,
                REPORT_WINDOW_CLOSED, AUTHORIZATION_STILL_VALID,
                MANDATE_INVALID, MANDATE_INCOMPLETE, MANDATE_NOT_ACTIVATABLE, MANDATE_NOT_ACTIVE, MANDATE_SUSPENDED,
                MANDATE_NOT_SUSPENDED, MANDATE_REVOKED,
                NOTHING_TO_ACTIVATE, VERSION_EXISTS, UNKNOWN_PRINCIPAL, BENEFICIARY_EXISTS, POLICY_INVALID, POLICY_RETIRED,
                RANGE_TOO_LARGE,
                LAST_ADMIN_KEY, INTERNAL
            detail (str | Unset):
            errors (list[ProblemErrorsItem] | Unset):
     """

    type_: str
    title: str
    status: int
    code: str
    detail: str | Unset = UNSET
    errors: list[ProblemErrorsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.problem_errors_item import ProblemErrorsItem # noqa: PLC0415
        type_ = self.type_

        title = self.title

        status = self.status

        code = self.code

        detail = self.detail

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
            "title": title,
            "status": status,
            "code": code,
        })
        if detail is not UNSET:
            field_dict["detail"] = detail
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.problem_errors_item import ProblemErrorsItem # noqa: PLC0415
        d = dict(src_dict)
        type_ = d.pop("type")

        title = d.pop("title")

        status = d.pop("status")

        code = d.pop("code")

        detail = d.pop("detail", UNSET)

        _errors = d.pop("errors", UNSET)
        errors: list[ProblemErrorsItem] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = ProblemErrorsItem.from_dict(errors_item_data)



                errors.append(errors_item)


        problem = cls(
            type_=type_,
            title=title,
            status=status,
            code=code,
            detail=detail,
            errors=errors,
        )


        problem.additional_properties = d
        return problem

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
