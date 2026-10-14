from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.json_rpc_message_error import JsonRpcMessageError
  from ..models.json_rpc_message_params import JsonRpcMessageParams
  from ..models.json_rpc_message_result import JsonRpcMessageResult





T = TypeVar("T", bound="JsonRpcMessage")



@_attrs_define
class JsonRpcMessage:
    """ A JSON-RPC 2.0 request, notification, result or error object (https://www.jsonrpc.org/specification)

        Attributes:
            jsonrpc (Literal['2.0']):
            id (int | None | str | Unset):
            method (str | Unset):
            params (JsonRpcMessageParams | Unset):
            result (JsonRpcMessageResult | Unset):
            error (JsonRpcMessageError | Unset):
     """

    jsonrpc: Literal['2.0']
    id: int | None | str | Unset = UNSET
    method: str | Unset = UNSET
    params: JsonRpcMessageParams | Unset = UNSET
    result: JsonRpcMessageResult | Unset = UNSET
    error: JsonRpcMessageError | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.json_rpc_message_error import JsonRpcMessageError # noqa: PLC0415
        from ..models.json_rpc_message_params import JsonRpcMessageParams # noqa: PLC0415
        from ..models.json_rpc_message_result import JsonRpcMessageResult # noqa: PLC0415
        jsonrpc = self.jsonrpc

        id: int | None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        method = self.method

        params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "jsonrpc": jsonrpc,
        })
        if id is not UNSET:
            field_dict["id"] = id
        if method is not UNSET:
            field_dict["method"] = method
        if params is not UNSET:
            field_dict["params"] = params
        if result is not UNSET:
            field_dict["result"] = result
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.json_rpc_message_error import JsonRpcMessageError # noqa: PLC0415
        from ..models.json_rpc_message_params import JsonRpcMessageParams # noqa: PLC0415
        from ..models.json_rpc_message_result import JsonRpcMessageResult # noqa: PLC0415
        d = dict(src_dict)
        jsonrpc = cast(Literal['2.0'] , d.pop("jsonrpc"))
        if jsonrpc != '2.0':
            raise ValueError(f"jsonrpc must match const '2.0', got '{jsonrpc}'")

        def _parse_id(data: object) -> int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))


        method = d.pop("method", UNSET)

        _params = d.pop("params", UNSET)
        params: JsonRpcMessageParams | Unset
        if isinstance(_params,  Unset):
            params = UNSET
        else:
            params = JsonRpcMessageParams.from_dict(_params)




        _result = d.pop("result", UNSET)
        result: JsonRpcMessageResult | Unset
        if isinstance(_result,  Unset):
            result = UNSET
        else:
            result = JsonRpcMessageResult.from_dict(_result)




        _error = d.pop("error", UNSET)
        error: JsonRpcMessageError | Unset
        if isinstance(_error,  Unset):
            error = UNSET
        else:
            error = JsonRpcMessageError.from_dict(_error)




        json_rpc_message = cls(
            jsonrpc=jsonrpc,
            id=id,
            method=method,
            params=params,
            result=result,
            error=error,
        )


        json_rpc_message.additional_properties = d
        return json_rpc_message

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
