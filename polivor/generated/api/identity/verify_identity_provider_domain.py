from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.identity_provider import IdentityProvider
from ...models.problem import Problem
from typing import cast
from uuid import UUID



def _get_kwargs(
    id: UUID,
    domain: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/identity-providers/{id}/domains/{domain}/verify".format(id=quote(str(id), safe=""),domain=quote(str(domain), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> IdentityProvider | Problem | None:
    if response.status_code == 200:
        response_200 = IdentityProvider.from_dict(response.json())



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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[IdentityProvider | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    domain: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[IdentityProvider | Problem]:
    """ Looks for the TXT record of the domain. A verified domain routes its email addresses to this
    provider; a domain is verified for one tenant only.

    Args:
        id (UUID):
        domain (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdentityProvider | Problem]
     """


    kwargs = _get_kwargs(
        id=id,
domain=domain,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: UUID,
    domain: str,
    *,
    client: AuthenticatedClient | Client,

) -> IdentityProvider | Problem | None:
    """ Looks for the TXT record of the domain. A verified domain routes its email addresses to this
    provider; a domain is verified for one tenant only.

    Args:
        id (UUID):
        domain (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdentityProvider | Problem
     """


    return sync_detailed(
        id=id,
domain=domain,
client=client,

    ).parsed

async def asyncio_detailed(
    id: UUID,
    domain: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[IdentityProvider | Problem]:
    """ Looks for the TXT record of the domain. A verified domain routes its email addresses to this
    provider; a domain is verified for one tenant only.

    Args:
        id (UUID):
        domain (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdentityProvider | Problem]
     """


    kwargs = _get_kwargs(
        id=id,
domain=domain,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: UUID,
    domain: str,
    *,
    client: AuthenticatedClient | Client,

) -> IdentityProvider | Problem | None:
    """ Looks for the TXT record of the domain. A verified domain routes its email addresses to this
    provider; a domain is verified for one tenant only.

    Args:
        id (UUID):
        domain (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdentityProvider | Problem
     """


    return (await asyncio_detailed(
        id=id,
domain=domain,
client=client,

    )).parsed
