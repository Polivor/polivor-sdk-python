from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.identity_provider import IdentityProvider
from ...models.identity_provider_create import IdentityProviderCreate
from ...models.problem import Problem
from typing import cast



def _get_kwargs(
    *,
    body: IdentityProviderCreate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/identity-providers",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> IdentityProvider | Problem | None:
    if response.status_code == 201:
        response_201 = IdentityProvider.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[IdentityProvider | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: IdentityProviderCreate,

) -> Response[IdentityProvider | Problem]:
    """ Registers the customer's identity provider for a production tenant, OpenID Connect or SAML 2.0. For
    OpenID Connect the issuer's discovery document is fetched and checked and the client secret is
    sealed and never shown again. For SAML the metadata (pasted or fetched from a URL) is checked and
    the response lists what to enter at the provider. Each domain must be verified with a DNS TXT record
    before it routes sign-ins.

    Args:
        body (IdentityProviderCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdentityProvider | Problem]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: IdentityProviderCreate,

) -> IdentityProvider | Problem | None:
    """ Registers the customer's identity provider for a production tenant, OpenID Connect or SAML 2.0. For
    OpenID Connect the issuer's discovery document is fetched and checked and the client secret is
    sealed and never shown again. For SAML the metadata (pasted or fetched from a URL) is checked and
    the response lists what to enter at the provider. Each domain must be verified with a DNS TXT record
    before it routes sign-ins.

    Args:
        body (IdentityProviderCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdentityProvider | Problem
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: IdentityProviderCreate,

) -> Response[IdentityProvider | Problem]:
    """ Registers the customer's identity provider for a production tenant, OpenID Connect or SAML 2.0. For
    OpenID Connect the issuer's discovery document is fetched and checked and the client secret is
    sealed and never shown again. For SAML the metadata (pasted or fetched from a URL) is checked and
    the response lists what to enter at the provider. Each domain must be verified with a DNS TXT record
    before it routes sign-ins.

    Args:
        body (IdentityProviderCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdentityProvider | Problem]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: IdentityProviderCreate,

) -> IdentityProvider | Problem | None:
    """ Registers the customer's identity provider for a production tenant, OpenID Connect or SAML 2.0. For
    OpenID Connect the issuer's discovery document is fetched and checked and the client secret is
    sealed and never shown again. For SAML the metadata (pasted or fetched from a URL) is checked and
    the response lists what to enter at the provider. Each domain must be verified with a DNS TXT record
    before it routes sign-ins.

    Args:
        body (IdentityProviderCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdentityProvider | Problem
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
