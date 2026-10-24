from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.user_role_role import UserRoleRole






T = TypeVar("T", bound="UserRole")



@_attrs_define
class UserRole:
    """ 
        Attributes:
            role (UserRoleRole): VIEWER reads; APPROVER also approves mandate versions; ADMIN does everything
     """

    role: UserRoleRole





    def to_dict(self) -> dict[str, Any]:
        role = self.role.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "role": role,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        role = UserRoleRole(d.pop("role"))




        user_role = cls(
            role=role,
        )

        return user_role

