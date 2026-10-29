from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.action import Action
  from ..models.signals import Signals





T = TypeVar("T", bound="SimulateRequest")



@_attrs_define
class SimulateRequest:
    """ 
        Attributes:
            action (Action): Unknown fields are ignored and never influence the decision.
            agent_id (UUID):
            agent_build (str | Unset): Informational label of the agent build or model. Stored in the decision and the
                evidence; it never changes an outcome.
            signals (Signals | Unset): Agent-supplied; may only be used in forbid rules (signals tighten, never loosen).
                Unknown fields are ignored.
            policy_version (int | Unset): Preview this policy version (a draft before publishing). Default: the active one.
     """

    action: Action
    agent_id: UUID
    agent_build: str | Unset = UNSET
    signals: Signals | Unset = UNSET
    policy_version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.action import Action # noqa: PLC0415
        from ..models.signals import Signals # noqa: PLC0415
        action = self.action.to_dict()

        agent_id = str(self.agent_id)

        agent_build = self.agent_build

        signals: dict[str, Any] | Unset = UNSET
        if not isinstance(self.signals, Unset):
            signals = self.signals.to_dict()

        policy_version = self.policy_version


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "action": action,
            "agent_id": agent_id,
        })
        if agent_build is not UNSET:
            field_dict["agent_build"] = agent_build
        if signals is not UNSET:
            field_dict["signals"] = signals
        if policy_version is not UNSET:
            field_dict["policy_version"] = policy_version

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action import Action # noqa: PLC0415
        from ..models.signals import Signals # noqa: PLC0415
        d = dict(src_dict)
        action = Action.from_dict(d.pop("action"))




        agent_id = UUID(d.pop("agent_id"))




        agent_build = d.pop("agent_build", UNSET)

        _signals = d.pop("signals", UNSET)
        signals: Signals | Unset
        if isinstance(_signals,  Unset):
            signals = UNSET
        else:
            signals = Signals.from_dict(_signals)




        policy_version = d.pop("policy_version", UNSET)

        simulate_request = cls(
            action=action,
            agent_id=agent_id,
            agent_build=agent_build,
            signals=signals,
            policy_version=policy_version,
        )


        simulate_request.additional_properties = d
        return simulate_request

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
