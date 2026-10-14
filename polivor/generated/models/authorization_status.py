from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.authorization_status_status import AuthorizationStatusStatus
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="AuthorizationStatus")



@_attrs_define
class AuthorizationStatus:
    """ 
        Attributes:
            id (UUID):
            status (AuthorizationStatusStatus):
            reported_at (datetime.datetime | None | Unset):
            external_ref (None | str | Unset):
     """

    id: UUID
    status: AuthorizationStatusStatus
    reported_at: datetime.datetime | None | Unset = UNSET
    external_ref: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        status = self.status.value

        reported_at: None | str | Unset
        if isinstance(self.reported_at, Unset):
            reported_at = UNSET
        elif isinstance(self.reported_at, datetime.datetime):
            reported_at = self.reported_at.isoformat()
        else:
            reported_at = self.reported_at

        external_ref: None | str | Unset
        if isinstance(self.external_ref, Unset):
            external_ref = UNSET
        else:
            external_ref = self.external_ref


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "status": status,
        })
        if reported_at is not UNSET:
            field_dict["reported_at"] = reported_at
        if external_ref is not UNSET:
            field_dict["external_ref"] = external_ref

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        status = AuthorizationStatusStatus(d.pop("status"))




        def _parse_reported_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reported_at_type_0 = datetime.datetime.fromisoformat(data)



                return reported_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        reported_at = _parse_reported_at(d.pop("reported_at", UNSET))


        def _parse_external_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_ref = _parse_external_ref(d.pop("external_ref", UNSET))


        authorization_status = cls(
            id=id,
            status=status,
            reported_at=reported_at,
            external_ref=external_ref,
        )


        authorization_status.additional_properties = d
        return authorization_status

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
