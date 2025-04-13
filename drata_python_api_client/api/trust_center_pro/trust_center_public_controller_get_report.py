from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.exception_response_dto import ExceptionResponseDto
from ...models.trust_center_public_controller_get_report_report_type import (
    TrustCenterPublicControllerGetReportReportType,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    start_date: str,
    end_date: str,
    workspace_id: float,
    report_type: TrustCenterPublicControllerGetReportReportType,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["startDate"] = start_date

    params["endDate"] = end_date

    params["workspaceId"] = workspace_id

    json_report_type = report_type.value
    params["reportType"] = json_report_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/trust-center/reports",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ExceptionResponseDto]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
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
) -> Response[Union[Any, ExceptionResponseDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start_date: str,
    end_date: str,
    workspace_id: float,
    report_type: TrustCenterPublicControllerGetReportReportType,
) -> Response[Union[Any, ExceptionResponseDto]]:
    """Retrieves CSV data for single Trust Center report

     Generate Trust Center Report Csv

    Args:
        start_date (str):  Example: 2025-07-01T16:45:55.246Z.
        end_date (str):  Example: 2025-07-01T16:45:55.246Z.
        workspace_id (float):  Example: 1.
        report_type (TrustCenterPublicControllerGetReportReportType):  Example: SUMMARY.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponseDto]]
    """

    kwargs = _get_kwargs(
        start_date=start_date,
        end_date=end_date,
        workspace_id=workspace_id,
        report_type=report_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    start_date: str,
    end_date: str,
    workspace_id: float,
    report_type: TrustCenterPublicControllerGetReportReportType,
) -> Optional[Union[Any, ExceptionResponseDto]]:
    """Retrieves CSV data for single Trust Center report

     Generate Trust Center Report Csv

    Args:
        start_date (str):  Example: 2025-07-01T16:45:55.246Z.
        end_date (str):  Example: 2025-07-01T16:45:55.246Z.
        workspace_id (float):  Example: 1.
        report_type (TrustCenterPublicControllerGetReportReportType):  Example: SUMMARY.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponseDto]
    """

    return sync_detailed(
        client=client,
        start_date=start_date,
        end_date=end_date,
        workspace_id=workspace_id,
        report_type=report_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_date: str,
    end_date: str,
    workspace_id: float,
    report_type: TrustCenterPublicControllerGetReportReportType,
) -> Response[Union[Any, ExceptionResponseDto]]:
    """Retrieves CSV data for single Trust Center report

     Generate Trust Center Report Csv

    Args:
        start_date (str):  Example: 2025-07-01T16:45:55.246Z.
        end_date (str):  Example: 2025-07-01T16:45:55.246Z.
        workspace_id (float):  Example: 1.
        report_type (TrustCenterPublicControllerGetReportReportType):  Example: SUMMARY.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponseDto]]
    """

    kwargs = _get_kwargs(
        start_date=start_date,
        end_date=end_date,
        workspace_id=workspace_id,
        report_type=report_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    start_date: str,
    end_date: str,
    workspace_id: float,
    report_type: TrustCenterPublicControllerGetReportReportType,
) -> Optional[Union[Any, ExceptionResponseDto]]:
    """Retrieves CSV data for single Trust Center report

     Generate Trust Center Report Csv

    Args:
        start_date (str):  Example: 2025-07-01T16:45:55.246Z.
        end_date (str):  Example: 2025-07-01T16:45:55.246Z.
        workspace_id (float):  Example: 1.
        report_type (TrustCenterPublicControllerGetReportReportType):  Example: SUMMARY.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponseDto]
    """

    return (
        await asyncio_detailed(
            client=client,
            start_date=start_date,
            end_date=end_date,
            workspace_id=workspace_id,
            report_type=report_type,
        )
    ).parsed
