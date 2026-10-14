from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.simulate_response_outcome import SimulateResponseOutcome
from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.check import Check
  from ..models.simulate_response_mandate import SimulateResponseMandate





T = TypeVar("T", bound="SimulateResponse")



@_attrs_define
class SimulateResponse:
    """ 
        Attributes:
            simulated (Literal[True]):
            outcome (SimulateResponseOutcome):
            reasons (list[Any]):
            checks (list[Check]):
            policy_version (int): 0 when no policy applied
            mandate (SimulateResponseMandate | Unset):
     """

    simulated: Literal[True]
    outcome: SimulateResponseOutcome
    reasons: list[Any]
    checks: list[Check]
    policy_version: int
    mandate: SimulateResponseMandate | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.check import Check # noqa: PLC0415
        from ..models.simulate_response_mandate import SimulateResponseMandate # noqa: PLC0415
        simulated = self.simulated

        outcome = self.outcome.value

        reasons = []
        for reasons_item_data in self.reasons:
            reasons_item: Any
            reasons_item = reasons_item_data
            reasons.append(reasons_item)



        checks = []
        for checks_item_data in self.checks:
            checks_item = checks_item_data.to_dict()
            checks.append(checks_item)



        policy_version = self.policy_version

        mandate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mandate, Unset):
            mandate = self.mandate.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "simulated": simulated,
            "outcome": outcome,
            "reasons": reasons,
            "checks": checks,
            "policy_version": policy_version,
        })
        if mandate is not UNSET:
            field_dict["mandate"] = mandate

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.check import Check # noqa: PLC0415
        from ..models.simulate_response_mandate import SimulateResponseMandate # noqa: PLC0415
        d = dict(src_dict)
        simulated = cast(Literal[True] , d.pop("simulated"))
        if simulated != True:
            raise ValueError(f"simulated must match const True, got '{simulated}'")

        outcome = SimulateResponseOutcome(d.pop("outcome"))




        reasons = []
        _reasons = d.pop("reasons")
        for reasons_item_data in (_reasons):
            def _parse_reasons_item(data: object) -> Any:
                return cast(Any, data)

            reasons_item = _parse_reasons_item(reasons_item_data)

            reasons.append(reasons_item)


        checks = []
        _checks = d.pop("checks")
        for checks_item_data in (_checks):
            checks_item = Check.from_dict(checks_item_data)



            checks.append(checks_item)


        policy_version = d.pop("policy_version")

        _mandate = d.pop("mandate", UNSET)
        mandate: SimulateResponseMandate | Unset
        if isinstance(_mandate,  Unset):
            mandate = UNSET
        else:
            mandate = SimulateResponseMandate.from_dict(_mandate)




        simulate_response = cls(
            simulated=simulated,
            outcome=outcome,
            reasons=reasons,
            checks=checks,
            policy_version=policy_version,
            mandate=mandate,
        )


        simulate_response.additional_properties = d
        return simulate_response

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
