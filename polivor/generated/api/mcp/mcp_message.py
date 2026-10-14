from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.json_rpc_message import JsonRpcMessage
from ...models.mcp_message_mcp_protocol_version import McpMessageMCPProtocolVersion
from ...models.problem import Problem
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: JsonRpcMessage,
    mcp_protocol_version: McpMessageMCPProtocolVersion | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(mcp_protocol_version, Unset):
        headers["MCP-Protocol-Version"] = str(mcp_protocol_version)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/mcp",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | JsonRpcMessage | Problem | None:
    if response.status_code == 200:
        response_200 = JsonRpcMessage.from_dict(response.json())



        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    if response.status_code == 400:
        response_400 = Problem.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Problem.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = Problem.from_dict(response.json())



        return response_403

    if response.status_code == 429:
        response_429 = Problem.from_dict(response.json())



        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | JsonRpcMessage | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: JsonRpcMessage,
    mcp_protocol_version: McpMessageMCPProtocolVersion | Unset = UNSET,

) -> Response[Any | JsonRpcMessage | Problem]:
    """ Model Context Protocol server with the tools authorize and get_decision (role agent)

     MCP over Streamable HTTP, answered as plain JSON (no event stream, no sessions): one JSON-RPC 2.0
    message per POST. Supported methods:
    `initialize`, `ping`, `tools/list` and `tools/call`; notifications get `202`. Protocol versions
    2025-06-18, 2025-03-26 and 2024-11-05.
    The tool `authorize` takes the fields of `AuthorizeRequest` plus a required `idempotency_key`;
    `get_decision` takes `decision_id`. A tool
    result carries the same JSON as the REST response (as `structuredContent` and as text); a business
    error is a tool result with
    `isError: true` holding a problem details object. Same API keys, roles and rate limits as `/v1`.
    Requests with an `Origin` header are
    refused (MCP clients are programs, not web pages). `GET` is not supported (405).

    Args:
        mcp_protocol_version (McpMessageMCPProtocolVersion | Unset):
        body (JsonRpcMessage): A JSON-RPC 2.0 request, notification, result or error object
            (https://www.jsonrpc.org/specification)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | JsonRpcMessage | Problem]
     """


    kwargs = _get_kwargs(
        body=body,
mcp_protocol_version=mcp_protocol_version,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: JsonRpcMessage,
    mcp_protocol_version: McpMessageMCPProtocolVersion | Unset = UNSET,

) -> Any | JsonRpcMessage | Problem | None:
    """ Model Context Protocol server with the tools authorize and get_decision (role agent)

     MCP over Streamable HTTP, answered as plain JSON (no event stream, no sessions): one JSON-RPC 2.0
    message per POST. Supported methods:
    `initialize`, `ping`, `tools/list` and `tools/call`; notifications get `202`. Protocol versions
    2025-06-18, 2025-03-26 and 2024-11-05.
    The tool `authorize` takes the fields of `AuthorizeRequest` plus a required `idempotency_key`;
    `get_decision` takes `decision_id`. A tool
    result carries the same JSON as the REST response (as `structuredContent` and as text); a business
    error is a tool result with
    `isError: true` holding a problem details object. Same API keys, roles and rate limits as `/v1`.
    Requests with an `Origin` header are
    refused (MCP clients are programs, not web pages). `GET` is not supported (405).

    Args:
        mcp_protocol_version (McpMessageMCPProtocolVersion | Unset):
        body (JsonRpcMessage): A JSON-RPC 2.0 request, notification, result or error object
            (https://www.jsonrpc.org/specification)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | JsonRpcMessage | Problem
     """


    return sync_detailed(
        client=client,
body=body,
mcp_protocol_version=mcp_protocol_version,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: JsonRpcMessage,
    mcp_protocol_version: McpMessageMCPProtocolVersion | Unset = UNSET,

) -> Response[Any | JsonRpcMessage | Problem]:
    """ Model Context Protocol server with the tools authorize and get_decision (role agent)

     MCP over Streamable HTTP, answered as plain JSON (no event stream, no sessions): one JSON-RPC 2.0
    message per POST. Supported methods:
    `initialize`, `ping`, `tools/list` and `tools/call`; notifications get `202`. Protocol versions
    2025-06-18, 2025-03-26 and 2024-11-05.
    The tool `authorize` takes the fields of `AuthorizeRequest` plus a required `idempotency_key`;
    `get_decision` takes `decision_id`. A tool
    result carries the same JSON as the REST response (as `structuredContent` and as text); a business
    error is a tool result with
    `isError: true` holding a problem details object. Same API keys, roles and rate limits as `/v1`.
    Requests with an `Origin` header are
    refused (MCP clients are programs, not web pages). `GET` is not supported (405).

    Args:
        mcp_protocol_version (McpMessageMCPProtocolVersion | Unset):
        body (JsonRpcMessage): A JSON-RPC 2.0 request, notification, result or error object
            (https://www.jsonrpc.org/specification)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | JsonRpcMessage | Problem]
     """


    kwargs = _get_kwargs(
        body=body,
mcp_protocol_version=mcp_protocol_version,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: JsonRpcMessage,
    mcp_protocol_version: McpMessageMCPProtocolVersion | Unset = UNSET,

) -> Any | JsonRpcMessage | Problem | None:
    """ Model Context Protocol server with the tools authorize and get_decision (role agent)

     MCP over Streamable HTTP, answered as plain JSON (no event stream, no sessions): one JSON-RPC 2.0
    message per POST. Supported methods:
    `initialize`, `ping`, `tools/list` and `tools/call`; notifications get `202`. Protocol versions
    2025-06-18, 2025-03-26 and 2024-11-05.
    The tool `authorize` takes the fields of `AuthorizeRequest` plus a required `idempotency_key`;
    `get_decision` takes `decision_id`. A tool
    result carries the same JSON as the REST response (as `structuredContent` and as text); a business
    error is a tool result with
    `isError: true` holding a problem details object. Same API keys, roles and rate limits as `/v1`.
    Requests with an `Origin` header are
    refused (MCP clients are programs, not web pages). `GET` is not supported (405).

    Args:
        mcp_protocol_version (McpMessageMCPProtocolVersion | Unset):
        body (JsonRpcMessage): A JSON-RPC 2.0 request, notification, result or error object
            (https://www.jsonrpc.org/specification)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | JsonRpcMessage | Problem
     """


    return (await asyncio_detailed(
        client=client,
body=body,
mcp_protocol_version=mcp_protocol_version,

    )).parsed
