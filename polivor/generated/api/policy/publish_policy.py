from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.policy_version import PolicyVersion
from ...models.problem import Problem
from typing import cast



def _get_kwargs(
    version: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/policies/{version}/publish".format(version=quote(str(version), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PolicyVersion | Problem | None:
    if response.status_code == 200:
        response_200 = PolicyVersion.from_dict(response.json())



        return response_200

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PolicyVersion | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    version: int,
    *,
    client: AuthenticatedClient | Client,

) -> Response[PolicyVersion | Problem]:
    """ Publish; immutable afterwards. Rejected if a permit rule references signals

    Args:
        version (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PolicyVersion | Problem]
     """


    kwargs = _get_kwargs(
        version=version,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    version: int,
    *,
    client: AuthenticatedClient | Client,

) -> PolicyVersion | Problem | None:
    """ Publish; immutable afterwards. Rejected if a permit rule references signals

    Args:
        version (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PolicyVersion | Problem
     """


    return sync_detailed(
        version=version,
client=client,

    ).parsed

async def asyncio_detailed(
    version: int,
    *,
    client: AuthenticatedClient | Client,

) -> Response[PolicyVersion | Problem]:
    """ Publish; immutable afterwards. Rejected if a permit rule references signals

    Args:
        version (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PolicyVersion | Problem]
     """


    kwargs = _get_kwargs(
        version=version,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    version: int,
    *,
    client: AuthenticatedClient | Client,

) -> PolicyVersion | Problem | None:
    """ Publish; immutable afterwards. Rejected if a permit rule references signals

    Args:
        version (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PolicyVersion | Problem
     """


    return (await asyncio_detailed(
        version=version,
client=client,

    )).parsed
