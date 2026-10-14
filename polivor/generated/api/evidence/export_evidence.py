from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.evidence_bundle import EvidenceBundle
from ...models.problem import Problem
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    from_seq: int | Unset = UNSET,
    to_seq: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["from_seq"] = from_seq

    params["to_seq"] = to_seq


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/evidence/export",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> EvidenceBundle | Problem | None:
    if response.status_code == 200:
        response_200 = EvidenceBundle.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Problem.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = Problem.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = Problem.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[EvidenceBundle | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_seq: int | Unset = UNSET,
    to_seq: int | Unset = UNSET,

) -> Response[EvidenceBundle | Problem]:
    """ Bundle for a range - rows, JWS, chain hashes and JWKS - verifiable offline

     At most 10000 rows per export (422 RANGE_TOO_LARGE otherwise).

    Args:
        from_seq (int | Unset):
        to_seq (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EvidenceBundle | Problem]
     """


    kwargs = _get_kwargs(
        from_seq=from_seq,
to_seq=to_seq,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    from_seq: int | Unset = UNSET,
    to_seq: int | Unset = UNSET,

) -> EvidenceBundle | Problem | None:
    """ Bundle for a range - rows, JWS, chain hashes and JWKS - verifiable offline

     At most 10000 rows per export (422 RANGE_TOO_LARGE otherwise).

    Args:
        from_seq (int | Unset):
        to_seq (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EvidenceBundle | Problem
     """


    return sync_detailed(
        client=client,
from_seq=from_seq,
to_seq=to_seq,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_seq: int | Unset = UNSET,
    to_seq: int | Unset = UNSET,

) -> Response[EvidenceBundle | Problem]:
    """ Bundle for a range - rows, JWS, chain hashes and JWKS - verifiable offline

     At most 10000 rows per export (422 RANGE_TOO_LARGE otherwise).

    Args:
        from_seq (int | Unset):
        to_seq (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EvidenceBundle | Problem]
     """


    kwargs = _get_kwargs(
        from_seq=from_seq,
to_seq=to_seq,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    from_seq: int | Unset = UNSET,
    to_seq: int | Unset = UNSET,

) -> EvidenceBundle | Problem | None:
    """ Bundle for a range - rows, JWS, chain hashes and JWKS - verifiable offline

     At most 10000 rows per export (422 RANGE_TOO_LARGE otherwise).

    Args:
        from_seq (int | Unset):
        to_seq (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EvidenceBundle | Problem
     """


    return (await asyncio_detailed(
        client=client,
from_seq=from_seq,
to_seq=to_seq,

    )).parsed
