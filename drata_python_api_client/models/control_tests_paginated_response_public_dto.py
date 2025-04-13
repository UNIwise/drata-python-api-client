from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.control_test_response_public_dto import ControlTestResponsePublicDto


T = TypeVar("T", bound="ControlTestsPaginatedResponsePublicDto")


@_attrs_define
class ControlTestsPaginatedResponsePublicDto:
    """
    Attributes:
        data (list['ControlTestResponsePublicDto']): Data set based on the pagination limits
        page (float): Which page of data are you requesting Example: 1.
        limit (float): How many items are you requesting Example: 10.
        total (float): How many items are in the overall set Example: 100.
    """

    data: list["ControlTestResponsePublicDto"]
    page: float
    limit: float
    total: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        page = self.page

        limit = self.limit

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "page": page,
                "limit": limit,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.control_test_response_public_dto import ControlTestResponsePublicDto

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = ControlTestResponsePublicDto.from_dict(data_item_data)

            data.append(data_item)

        page = d.pop("page")

        limit = d.pop("limit")

        total = d.pop("total")

        control_tests_paginated_response_public_dto = cls(
            data=data,
            page=page,
            limit=limit,
            total=total,
        )

        control_tests_paginated_response_public_dto.additional_properties = d
        return control_tests_paginated_response_public_dto

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
