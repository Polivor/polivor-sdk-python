from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.api_key_role import ApiKeyRole
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="ApiKey")



@_attrs_define
class ApiKey:
    """ 
        Attributes:
            id (UUID):
            role (ApiKeyRole):
            prefix (str): The non-secret part (pv_test_<prefix> or pv_live_<prefix>) that identifies the key in logs
            created_at (datetime.datetime):
            agent_id (None | str | Unset):
            revoked_at (datetime.datetime | None | Unset):
     """

    id: UUID
    role: ApiKeyRole
    prefix: str
    created_at: datetime.datetime
    agent_id: None | str | Unset = UNSET
    revoked_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        role = self.role.value

        prefix = self.prefix

        created_at = self.created_at.isoformat()

        agent_id: None | str | Unset
        if isinstance(self.agent_id, Unset):
            agent_id = UNSET
        else:
            agent_id = self.agent_id

        revoked_at: None | str | Unset
        if isinstance(self.revoked_at, Unset):
            revoked_at = UNSET
        elif isinstance(self.revoked_at, datetime.datetime):
            revoked_at = self.revoked_at.isoformat()
        else:
            revoked_at = self.revoked_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "role": role,
            "prefix": prefix,
            "created_at": created_at,
        })
        if agent_id is not UNSET:
            field_dict["agent_id"] = agent_id
        if revoked_at is not UNSET:
            field_dict["revoked_at"] = revoked_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        role = ApiKeyRole(d.pop("role"))




        prefix = d.pop("prefix")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))




        def _parse_agent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        agent_id = _parse_agent_id(d.pop("agent_id", UNSET))


        def _parse_revoked_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                revoked_at_type_0 = datetime.datetime.fromisoformat(data)



                return revoked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        revoked_at = _parse_revoked_at(d.pop("revoked_at", UNSET))


        api_key = cls(
            id=id,
            role=role,
            prefix=prefix,
            created_at=created_at,
            agent_id=agent_id,
            revoked_at=revoked_at,
        )


        api_key.additional_properties = d
        return api_key

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
