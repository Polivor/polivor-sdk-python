from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mandate import Mandate
from ...models.mandate_body import MandateBody
from ...models.problem import Problem
from typing import cast
from uuid import UUID



def _get_kwargs(
    id: UUID,
    *,
    body: MandateBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/mandates/{id}/versions".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Mandate | Problem | None:
    if response.status_code == 201:
        response_201 = Mandate.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = Problem.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Problem.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = Problem.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = Problem.from_dict(response.json())



        return response_409

    if response.status_code == 422:
        response_422 = Problem.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Mandate | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: MandateBody,

) -> Response[Mandate | Problem]:
    """ Create the next version. Only the validity dates changed gives the next minor version (2.1 to 2.2);
    anything else the next major (2.1 to 3.0). The same body is refused (409 MANDATE_UNCHANGED).
    Versions are immutable.

    Args:
        id (UUID):
        body (MandateBody): Native Financial Mandate body. The authoritative definition is
            docs/schema/financial-mandate.v0.json; validated against it on write. A DRAFT imported
            from AP2 holds only the mapped fields until a complete version is added.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Mandate | Problem]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: MandateBody,

) -> Mandate | Problem | None:
    """ Create the next version. Only the validity dates changed gives the next minor version (2.1 to 2.2);
    anything else the next major (2.1 to 3.0). The same body is refused (409 MANDATE_UNCHANGED).
    Versions are immutable.

    Args:
        id (UUID):
        body (MandateBody): Native Financial Mandate body. The authoritative definition is
            docs/schema/financial-mandate.v0.json; validated against it on write. A DRAFT imported
            from AP2 holds only the mapped fields until a complete version is added.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Mandate | Problem
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: MandateBody,

) -> Response[Mandate | Problem]:
    """ Create the next version. Only the validity dates changed gives the next minor version (2.1 to 2.2);
    anything else the next major (2.1 to 3.0). The same body is refused (409 MANDATE_UNCHANGED).
    Versions are immutable.

    Args:
        id (UUID):
        body (MandateBody): Native Financial Mandate body. The authoritative definition is
            docs/schema/financial-mandate.v0.json; validated against it on write. A DRAFT imported
            from AP2 holds only the mapped fields until a complete version is added.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Mandate | Problem]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: MandateBody,

) -> Mandate | Problem | None:
    """ Create the next version. Only the validity dates changed gives the next minor version (2.1 to 2.2);
    anything else the next major (2.1 to 3.0). The same body is refused (409 MANDATE_UNCHANGED).
    Versions are immutable.

    Args:
        id (UUID):
        body (MandateBody): Native Financial Mandate body. The authoritative definition is
            docs/schema/financial-mandate.v0.json; validated against it on write. A DRAFT imported
            from AP2 holds only the mapped fields until a complete version is added.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Mandate | Problem
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
