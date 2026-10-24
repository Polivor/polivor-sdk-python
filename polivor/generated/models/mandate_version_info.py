from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="MandateVersionInfo")



@_attrs_define
class MandateVersionInfo:
    """ 
        Attributes:
            version (str): major.minor, for example 2.1. A major version changes the rules, a minor version only the
                validity dates.
            live (bool):
            revoked (bool):
            valid_from (datetime.datetime):
            valid_until (datetime.datetime):
            approver_person_id (None | UUID):
     """

    version: str
    live: bool
    revoked: bool
    valid_from: datetime.datetime
    valid_until: datetime.datetime
    approver_person_id: None | UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        version = self.version

        live = self.live

        revoked = self.revoked

        valid_from = self.valid_from.isoformat()

        valid_until = self.valid_until.isoformat()

        approver_person_id: None | str
        if isinstance(self.approver_person_id, UUID):
            approver_person_id = str(self.approver_person_id)
        else:
            approver_person_id = self.approver_person_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "version": version,
            "live": live,
            "revoked": revoked,
            "valid_from": valid_from,
            "valid_until": valid_until,
            "approver_person_id": approver_person_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        version = d.pop("version")

        live = d.pop("live")

        revoked = d.pop("revoked")

        valid_from = datetime.datetime.fromisoformat(d.pop("valid_from"))




        valid_until = datetime.datetime.fromisoformat(d.pop("valid_until"))




        def _parse_approver_person_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approver_person_id_type_0 = UUID(data)



                return approver_person_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        approver_person_id = _parse_approver_person_id(d.pop("approver_person_id"))


        mandate_version_info = cls(
            version=version,
            live=live,
            revoked=revoked,
            valid_from=valid_from,
            valid_until=valid_until,
            approver_person_id=approver_person_id,
        )


        mandate_version_info.additional_properties = d
        return mandate_version_info

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
