from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.authorize_request import AuthorizeRequest
from ...models.authorize_response import AuthorizeResponse
from ...models.problem import Problem
from typing import cast



def _get_kwargs(
    *,
    body: AuthorizeRequest,
    idempotency_key: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/authorize",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AuthorizeResponse | Problem | None:
    if response.status_code == 200:
        response_200 = AuthorizeResponse.from_dict(response.json())



        return response_200

    if response.status_code == 202:
        response_202 = AuthorizeResponse.from_dict(response.json())



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

    if response.status_code == 409:
        response_409 = Problem.from_dict(response.json())



        return response_409

    if response.status_code == 422:
        response_422 = Problem.from_dict(response.json())



        return response_422

    if response.status_code == 429:
        response_429 = Problem.from_dict(response.json())



        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AuthorizeResponse | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AuthorizeRequest,
    idempotency_key: str,

) -> Response[AuthorizeResponse | Problem]:
    """ Request authority for one action (role agent)

     400 IDEMPOTENCY_KEY_REQUIRED when the header is missing. 409 IDEMPOTENCY_KEY_REUSED when the key was
    used with a different body
    (or by another agent), and IDEMPOTENCY_KEY_EXPIRED once the 24 h retention is over. A replay returns
    the stored response unchanged.
    REQUIRE_APPROVAL reserves no budget; budget is reserved when the approval is granted.
    The answer never says why (ADR-025): no reasons, no checks, no policy version. When nothing is
    allowed it carries a coarse `denial` with a code from a closed list,
    a fixed sentence and `retryable`. A person sees the full explanation through the admin key, the
    console or the evidence.

    Args:
        idempotency_key (str):
        body (AuthorizeRequest): Unknown fields are ignored. Flags such as iban_changed or
            beneficiary_allowlisted have no effect, Polivor computes those facts itself.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuthorizeResponse | Problem]
     """


    kwargs = _get_kwargs(
        body=body,
idempotency_key=idempotency_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: AuthorizeRequest,
    idempotency_key: str,

) -> AuthorizeResponse | Problem | None:
    """ Request authority for one action (role agent)

     400 IDEMPOTENCY_KEY_REQUIRED when the header is missing. 409 IDEMPOTENCY_KEY_REUSED when the key was
    used with a different body
    (or by another agent), and IDEMPOTENCY_KEY_EXPIRED once the 24 h retention is over. A replay returns
    the stored response unchanged.
    REQUIRE_APPROVAL reserves no budget; budget is reserved when the approval is granted.
    The answer never says why (ADR-025): no reasons, no checks, no policy version. When nothing is
    allowed it carries a coarse `denial` with a code from a closed list,
    a fixed sentence and `retryable`. A person sees the full explanation through the admin key, the
    console or the evidence.

    Args:
        idempotency_key (str):
        body (AuthorizeRequest): Unknown fields are ignored. Flags such as iban_changed or
            beneficiary_allowlisted have no effect, Polivor computes those facts itself.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuthorizeResponse | Problem
     """


    return sync_detailed(
        client=client,
body=body,
idempotency_key=idempotency_key,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AuthorizeRequest,
    idempotency_key: str,

) -> Response[AuthorizeResponse | Problem]:
    """ Request authority for one action (role agent)

     400 IDEMPOTENCY_KEY_REQUIRED when the header is missing. 409 IDEMPOTENCY_KEY_REUSED when the key was
    used with a different body
    (or by another agent), and IDEMPOTENCY_KEY_EXPIRED once the 24 h retention is over. A replay returns
    the stored response unchanged.
    REQUIRE_APPROVAL reserves no budget; budget is reserved when the approval is granted.
    The answer never says why (ADR-025): no reasons, no checks, no policy version. When nothing is
    allowed it carries a coarse `denial` with a code from a closed list,
    a fixed sentence and `retryable`. A person sees the full explanation through the admin key, the
    console or the evidence.

    Args:
        idempotency_key (str):
        body (AuthorizeRequest): Unknown fields are ignored. Flags such as iban_changed or
            beneficiary_allowlisted have no effect, Polivor computes those facts itself.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuthorizeResponse | Problem]
     """


    kwargs = _get_kwargs(
        body=body,
idempotency_key=idempotency_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AuthorizeRequest,
    idempotency_key: str,

) -> AuthorizeResponse | Problem | None:
    """ Request authority for one action (role agent)

     400 IDEMPOTENCY_KEY_REQUIRED when the header is missing. 409 IDEMPOTENCY_KEY_REUSED when the key was
    used with a different body
    (or by another agent), and IDEMPOTENCY_KEY_EXPIRED once the 24 h retention is over. A replay returns
    the stored response unchanged.
    REQUIRE_APPROVAL reserves no budget; budget is reserved when the approval is granted.
    The answer never says why (ADR-025): no reasons, no checks, no policy version. When nothing is
    allowed it carries a coarse `denial` with a code from a closed list,
    a fixed sentence and `retryable`. A person sees the full explanation through the admin key, the
    console or the evidence.

    Args:
        idempotency_key (str):
        body (AuthorizeRequest): Unknown fields are ignored. Flags such as iban_changed or
            beneficiary_allowlisted have no effect, Polivor computes those facts itself.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuthorizeResponse | Problem
     """


    return (await asyncio_detailed(
        client=client,
body=body,
idempotency_key=idempotency_key,

    )).parsed
