from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.user_invite_role import UserInviteRole
from uuid import UUID






T = TypeVar("T", bound="UserInvite")



@_attrs_define
class UserInvite:
    """ 
        Attributes:
            person_id (UUID):
            role (UserInviteRole):
     """

    person_id: UUID
    role: UserInviteRole





    def to_dict(self) -> dict[str, Any]:
        person_id = str(self.person_id)

        role = self.role.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "person_id": person_id,
            "role": role,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        person_id = UUID(d.pop("person_id"))




        role = UserInviteRole(d.pop("role"))




        user_invite = cls(
            person_id=person_id,
            role=role,
        )

        return user_invite

