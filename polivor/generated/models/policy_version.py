from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.policy_version_status import PolicyVersionStatus
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.template_params import TemplateParams





T = TypeVar("T", bound="PolicyVersion")



@_attrs_define
class PolicyVersion:
    """ 
        Attributes:
            version (int):
            status (PolicyVersionStatus):
            cedar (str):
            cedar_sha256 (str): Hex
            id (UUID | Unset):
            template_params (None | TemplateParams | Unset):
            published_at (datetime.datetime | None | Unset):
     """

    version: int
    status: PolicyVersionStatus
    cedar: str
    cedar_sha256: str
    id: UUID | Unset = UNSET
    template_params: None | TemplateParams | Unset = UNSET
    published_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.template_params import TemplateParams # noqa: PLC0415
        version = self.version

        status = self.status.value

        cedar = self.cedar

        cedar_sha256 = self.cedar_sha256

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        template_params: dict[str, Any] | None | Unset
        if isinstance(self.template_params, Unset):
            template_params = UNSET
        elif isinstance(self.template_params, TemplateParams):
            template_params = self.template_params.to_dict()
        else:
            template_params = self.template_params

        published_at: None | str | Unset
        if isinstance(self.published_at, Unset):
            published_at = UNSET
        elif isinstance(self.published_at, datetime.datetime):
            published_at = self.published_at.isoformat()
        else:
            published_at = self.published_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "version": version,
            "status": status,
            "cedar": cedar,
            "cedar_sha256": cedar_sha256,
        })
        if id is not UNSET:
            field_dict["id"] = id
        if template_params is not UNSET:
            field_dict["template_params"] = template_params
        if published_at is not UNSET:
            field_dict["published_at"] = published_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_params import TemplateParams # noqa: PLC0415
        d = dict(src_dict)
        version = d.pop("version")

        status = PolicyVersionStatus(d.pop("status"))




        cedar = d.pop("cedar")

        cedar_sha256 = d.pop("cedar_sha256")

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_template_params(data: object) -> None | TemplateParams | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                template_params_type_0 = TemplateParams.from_dict(data)



                return template_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TemplateParams | Unset, data)

        template_params = _parse_template_params(d.pop("template_params", UNSET))


        def _parse_published_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                published_at_type_0 = datetime.datetime.fromisoformat(data)



                return published_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        published_at = _parse_published_at(d.pop("published_at", UNSET))


        policy_version = cls(
            version=version,
            status=status,
            cedar=cedar,
            cedar_sha256=cedar_sha256,
            id=id,
            template_params=template_params,
            published_at=published_at,
        )


        policy_version.additional_properties = d
        return policy_version

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
