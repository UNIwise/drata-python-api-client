from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.exception_response_dto import ExceptionResponseDto
from ...models.exception_response_public_dto import ExceptionResponsePublicDto
from ...models.user_identities_infrastructure_response_public_dto import UserIdentitiesInfrastructureResponsePublicDto
from ...models.user_identities_public_controller_list_infrastructure_users_identities_client_type import (
    UserIdentitiesPublicControllerListInfrastructureUsersIdentitiesClientType,
)
from ...models.user_identities_public_controller_list_infrastructure_users_identities_sort import (
    UserIdentitiesPublicControllerListInfrastructureUsersIdentitiesSort,
)
from ...models.user_identities_public_controller_list_infrastructure_users_identities_sort_dir import (
    UserIdentitiesPublicControllerListInfrastructureUsersIdentitiesSortDir,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: Union[Unset, float] = 1.0,
    limit: Union[Unset, float] = 20.0,
    q: Union[Unset, str] = UNSET,
    client_type: Union[Unset, UserIdentitiesPublicControllerListInfrastructureUsersIdentitiesClientType] = UNSET,
    connection_id: Union[Unset, float] = UNSET,
    sort: Union[Unset, UserIdentitiesPublicControllerListInfrastructureUsersIdentitiesSort] = UNSET,
    sort_dir: Union[Unset, UserIdentitiesPublicControllerListInfrastructureUsersIdentitiesSortDir] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    params["q"] = q

    json_client_type: Union[Unset, str] = UNSET
    if not isinstance(client_type, Unset):
        json_client_type = client_type.value

    params["clientType"] = json_client_type

    params["connectionId"] = connection_id

    json_sort: Union[Unset, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    json_sort_dir: Union[Unset, str] = UNSET
    if not isinstance(sort_dir, Unset):
        json_sort_dir = sort_dir.value

    params["sortDir"] = json_sort_dir

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/user-identities/infrastructure",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ExceptionResponseDto, ExceptionResponsePublicDto, UserIdentitiesInfrastructureResponsePublicDto]]:
    if response.status_code == 200:
        response_200 = UserIdentitiesInfrastructureResponsePublicDto.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionResponsePublicDto.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ExceptionResponseDto.from_dict(response.json())

        return response_401
    if response.status_code == 402:
        response_402 = ExceptionResponseDto.from_dict(response.json())

        return response_402
    if response.status_code == 403:
        response_403 = ExceptionResponseDto.from_dict(response.json())

        return response_403
    if response.status_code == 412:
        response_412 = ExceptionResponseDto.from_dict(response.json())

        return response_412
    if response.status_code == 500:
        response_500 = ExceptionResponseDto.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ExceptionResponseDto, ExceptionResponsePublicDto, UserIdentitiesInfrastructureResponsePublicDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, float] = 1.0,
    limit: Union[Unset, float] = 20.0,
    q: Union[Unset, str] = UNSET,
    client_type: Union[Unset, UserIdentitiesPublicControllerListInfrastructureUsersIdentitiesClientType] = UNSET,
    connection_id: Union[Unset, float] = UNSET,
    sort: Union[Unset, UserIdentitiesPublicControllerListInfrastructureUsersIdentitiesSort] = UNSET,
    sort_dir: Union[Unset, UserIdentitiesPublicControllerListInfrastructureUsersIdentitiesSortDir] = UNSET,
) -> Response[Union[ExceptionResponseDto, ExceptionResponsePublicDto, UserIdentitiesInfrastructureResponsePublicDto]]:
    """Find infrastructure user identities

     List infrastructure user identities by username or email

    Args:
        page (Union[Unset, float]):  Default: 1.0.
        limit (Union[Unset, float]):  Default: 20.0.
        q (Union[Unset, str]):  Example: 1a2b3c.
        client_type (Union[Unset,
            UserIdentitiesPublicControllerListInfrastructureUsersIdentitiesClientType]):  Example:
            AWS.
        connection_id (Union[Unset, float]):  Example: 1.
        sort (Union[Unset, UserIdentitiesPublicControllerListInfrastructureUsersIdentitiesSort]):
            Example: USERNAME.
        sort_dir (Union[Unset,
            UserIdentitiesPublicControllerListInfrastructureUsersIdentitiesSortDir]):  Example: ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExceptionResponseDto, ExceptionResponsePublicDto, UserIdentitiesInfrastructureResponsePublicDto]]
    """

    kwargs = _get_kwargs(
        page=page,
        limit=limit,
        q=q,
        client_type=client_type,
        connection_id=connection_id,
        sort=sort,
        sort_dir=sort_dir,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, float] = 1.0,
    limit: Union[Unset, float] = 20.0,
    q: Union[Unset, str] = UNSET,
    client_type: Union[Unset, UserIdentitiesPublicControllerListInfrastructureUsersIdentitiesClientType] = UNSET,
    connection_id: Union[Unset, float] = UNSET,
    sort: Union[Unset, UserIdentitiesPublicControllerListInfrastructureUsersIdentitiesSort] = UNSET,
    sort_dir: Union[Unset, UserIdentitiesPublicControllerListInfrastructureUsersIdentitiesSortDir] = UNSET,
) -> Optional[Union[ExceptionResponseDto, ExceptionResponsePublicDto, UserIdentitiesInfrastructureResponsePublicDto]]:
    """Find infrastructure user identities

     List infrastructure user identities by username or email

    Args:
        page (Union[Unset, float]):  Default: 1.0.
        limit (Union[Unset, float]):  Default: 20.0.
        q (Union[Unset, str]):  Example: 1a2b3c.
        client_type (Union[Unset,
            UserIdentitiesPublicControllerListInfrastructureUsersIdentitiesClientType]):  Example:
            AWS.
        connection_id (Union[Unset, float]):  Example: 1.
        sort (Union[Unset, UserIdentitiesPublicControllerListInfrastructureUsersIdentitiesSort]):
            Example: USERNAME.
        sort_dir (Union[Unset,
            UserIdentitiesPublicControllerListInfrastructureUsersIdentitiesSortDir]):  Example: ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExceptionResponseDto, ExceptionResponsePublicDto, UserIdentitiesInfrastructureResponsePublicDto]
    """

    return sync_detailed(
        client=client,
        page=page,
        limit=limit,
        q=q,
        client_type=client_type,
        connection_id=connection_id,
        sort=sort,
        sort_dir=sort_dir,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, float] = 1.0,
    limit: Union[Unset, float] = 20.0,
    q: Union[Unset, str] = UNSET,
    client_type: Union[Unset, UserIdentitiesPublicControllerListInfrastructureUsersIdentitiesClientType] = UNSET,
    connection_id: Union[Unset, float] = UNSET,
    sort: Union[Unset, UserIdentitiesPublicControllerListInfrastructureUsersIdentitiesSort] = UNSET,
    sort_dir: Union[Unset, UserIdentitiesPublicControllerListInfrastructureUsersIdentitiesSortDir] = UNSET,
) -> Response[Union[ExceptionResponseDto, ExceptionResponsePublicDto, UserIdentitiesInfrastructureResponsePublicDto]]:
    """Find infrastructure user identities

     List infrastructure user identities by username or email

    Args:
        page (Union[Unset, float]):  Default: 1.0.
        limit (Union[Unset, float]):  Default: 20.0.
        q (Union[Unset, str]):  Example: 1a2b3c.
        client_type (Union[Unset,
            UserIdentitiesPublicControllerListInfrastructureUsersIdentitiesClientType]):  Example:
            AWS.
        connection_id (Union[Unset, float]):  Example: 1.
        sort (Union[Unset, UserIdentitiesPublicControllerListInfrastructureUsersIdentitiesSort]):
            Example: USERNAME.
        sort_dir (Union[Unset,
            UserIdentitiesPublicControllerListInfrastructureUsersIdentitiesSortDir]):  Example: ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExceptionResponseDto, ExceptionResponsePublicDto, UserIdentitiesInfrastructureResponsePublicDto]]
    """

    kwargs = _get_kwargs(
        page=page,
        limit=limit,
        q=q,
        client_type=client_type,
        connection_id=connection_id,
        sort=sort,
        sort_dir=sort_dir,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, float] = 1.0,
    limit: Union[Unset, float] = 20.0,
    q: Union[Unset, str] = UNSET,
    client_type: Union[Unset, UserIdentitiesPublicControllerListInfrastructureUsersIdentitiesClientType] = UNSET,
    connection_id: Union[Unset, float] = UNSET,
    sort: Union[Unset, UserIdentitiesPublicControllerListInfrastructureUsersIdentitiesSort] = UNSET,
    sort_dir: Union[Unset, UserIdentitiesPublicControllerListInfrastructureUsersIdentitiesSortDir] = UNSET,
) -> Optional[Union[ExceptionResponseDto, ExceptionResponsePublicDto, UserIdentitiesInfrastructureResponsePublicDto]]:
    """Find infrastructure user identities

     List infrastructure user identities by username or email

    Args:
        page (Union[Unset, float]):  Default: 1.0.
        limit (Union[Unset, float]):  Default: 20.0.
        q (Union[Unset, str]):  Example: 1a2b3c.
        client_type (Union[Unset,
            UserIdentitiesPublicControllerListInfrastructureUsersIdentitiesClientType]):  Example:
            AWS.
        connection_id (Union[Unset, float]):  Example: 1.
        sort (Union[Unset, UserIdentitiesPublicControllerListInfrastructureUsersIdentitiesSort]):
            Example: USERNAME.
        sort_dir (Union[Unset,
            UserIdentitiesPublicControllerListInfrastructureUsersIdentitiesSortDir]):  Example: ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExceptionResponseDto, ExceptionResponsePublicDto, UserIdentitiesInfrastructureResponsePublicDto]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            limit=limit,
            q=q,
            client_type=client_type,
            connection_id=connection_id,
            sort=sort,
            sort_dir=sort_dir,
        )
    ).parsed
