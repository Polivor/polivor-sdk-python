from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.ap_2_import_result import Ap2ImportResult
from ...models.import_ap_2_mandate_body import ImportAp2MandateBody
from ...models.problem import Problem
from typing import cast



def _get_kwargs(
    *,
    body: ImportAp2MandateBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/mandates/import/ap2",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Ap2ImportResult | Problem | None:
    if response.status_code == 201:
        response_201 = Ap2ImportResult.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Ap2ImportResult | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ImportAp2MandateBody,

) -> Response[Ap2ImportResult | Problem]:
    """ Import an AP2 open payment mandate into a DRAFT native mandate (adapter; body at most 64 KB)

     Accepts an AP2 v0.2 Open Payment Mandate (`vct` mandate.payment.open.1) as an SD-JWT signed ES256 by
    a key of a trusted issuer
    (`POST /v1/trusted-issuers`). The signature, every disclosure and the expiry are checked. What AP2
    states precisely is copied
    (per-payment maximum as integer minor units and its currency, the validity window); everything else
    is listed in the report as
    not enforced natively or as still to complete. Principal and agent come from the request.

    **Constraints Polivor cannot enforce.** AP2 says a constraint a verifier does not understand must
    fail evaluation, and a native
    mandate is looser than the credential wherever it cannot enforce one. So an import that carries
    payees, a budget, recurrence,
    payment instruments, PISPs, a reference or a minimum amount is refused (422
    AP2_UNENFORCED_CONSTRAINTS, one error per type) until the
    request names each of them in `acknowledge_unenforced`; constraint types AP2 does not define at all
    are never imported
    (422 AP2_UNKNOWN_CONSTRAINT). Issuer keys are the ones registered for the issuer plus, if it has a
    `jwks_url`, the set published
    there at the time of the import (AP2_ISSUER_KEYS_UNAVAILABLE if that cannot be fetched). The DRAFT
    cannot be activated until a new
    version with the missing fields is created (`POST /v1/mandates/{id}/versions`). The raw credential
    and its hash are kept.

    Args:
        body (ImportAp2MandateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Ap2ImportResult | Problem]
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
    body: ImportAp2MandateBody,

) -> Ap2ImportResult | Problem | None:
    """ Import an AP2 open payment mandate into a DRAFT native mandate (adapter; body at most 64 KB)

     Accepts an AP2 v0.2 Open Payment Mandate (`vct` mandate.payment.open.1) as an SD-JWT signed ES256 by
    a key of a trusted issuer
    (`POST /v1/trusted-issuers`). The signature, every disclosure and the expiry are checked. What AP2
    states precisely is copied
    (per-payment maximum as integer minor units and its currency, the validity window); everything else
    is listed in the report as
    not enforced natively or as still to complete. Principal and agent come from the request.

    **Constraints Polivor cannot enforce.** AP2 says a constraint a verifier does not understand must
    fail evaluation, and a native
    mandate is looser than the credential wherever it cannot enforce one. So an import that carries
    payees, a budget, recurrence,
    payment instruments, PISPs, a reference or a minimum amount is refused (422
    AP2_UNENFORCED_CONSTRAINTS, one error per type) until the
    request names each of them in `acknowledge_unenforced`; constraint types AP2 does not define at all
    are never imported
    (422 AP2_UNKNOWN_CONSTRAINT). Issuer keys are the ones registered for the issuer plus, if it has a
    `jwks_url`, the set published
    there at the time of the import (AP2_ISSUER_KEYS_UNAVAILABLE if that cannot be fetched). The DRAFT
    cannot be activated until a new
    version with the missing fields is created (`POST /v1/mandates/{id}/versions`). The raw credential
    and its hash are kept.

    Args:
        body (ImportAp2MandateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Ap2ImportResult | Problem
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ImportAp2MandateBody,

) -> Response[Ap2ImportResult | Problem]:
    """ Import an AP2 open payment mandate into a DRAFT native mandate (adapter; body at most 64 KB)

     Accepts an AP2 v0.2 Open Payment Mandate (`vct` mandate.payment.open.1) as an SD-JWT signed ES256 by
    a key of a trusted issuer
    (`POST /v1/trusted-issuers`). The signature, every disclosure and the expiry are checked. What AP2
    states precisely is copied
    (per-payment maximum as integer minor units and its currency, the validity window); everything else
    is listed in the report as
    not enforced natively or as still to complete. Principal and agent come from the request.

    **Constraints Polivor cannot enforce.** AP2 says a constraint a verifier does not understand must
    fail evaluation, and a native
    mandate is looser than the credential wherever it cannot enforce one. So an import that carries
    payees, a budget, recurrence,
    payment instruments, PISPs, a reference or a minimum amount is refused (422
    AP2_UNENFORCED_CONSTRAINTS, one error per type) until the
    request names each of them in `acknowledge_unenforced`; constraint types AP2 does not define at all
    are never imported
    (422 AP2_UNKNOWN_CONSTRAINT). Issuer keys are the ones registered for the issuer plus, if it has a
    `jwks_url`, the set published
    there at the time of the import (AP2_ISSUER_KEYS_UNAVAILABLE if that cannot be fetched). The DRAFT
    cannot be activated until a new
    version with the missing fields is created (`POST /v1/mandates/{id}/versions`). The raw credential
    and its hash are kept.

    Args:
        body (ImportAp2MandateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Ap2ImportResult | Problem]
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
    body: ImportAp2MandateBody,

) -> Ap2ImportResult | Problem | None:
    """ Import an AP2 open payment mandate into a DRAFT native mandate (adapter; body at most 64 KB)

     Accepts an AP2 v0.2 Open Payment Mandate (`vct` mandate.payment.open.1) as an SD-JWT signed ES256 by
    a key of a trusted issuer
    (`POST /v1/trusted-issuers`). The signature, every disclosure and the expiry are checked. What AP2
    states precisely is copied
    (per-payment maximum as integer minor units and its currency, the validity window); everything else
    is listed in the report as
    not enforced natively or as still to complete. Principal and agent come from the request.

    **Constraints Polivor cannot enforce.** AP2 says a constraint a verifier does not understand must
    fail evaluation, and a native
    mandate is looser than the credential wherever it cannot enforce one. So an import that carries
    payees, a budget, recurrence,
    payment instruments, PISPs, a reference or a minimum amount is refused (422
    AP2_UNENFORCED_CONSTRAINTS, one error per type) until the
    request names each of them in `acknowledge_unenforced`; constraint types AP2 does not define at all
    are never imported
    (422 AP2_UNKNOWN_CONSTRAINT). Issuer keys are the ones registered for the issuer plus, if it has a
    `jwks_url`, the set published
    there at the time of the import (AP2_ISSUER_KEYS_UNAVAILABLE if that cannot be fetched). The DRAFT
    cannot be activated until a new
    version with the missing fields is created (`POST /v1/mandates/{id}/versions`). The raw credential
    and its hash are kept.

    Args:
        body (ImportAp2MandateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Ap2ImportResult | Problem
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
