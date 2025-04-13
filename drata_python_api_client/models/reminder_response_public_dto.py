import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ReminderResponsePublicDto")


@_attrs_define
class ReminderResponsePublicDto:
    """
    Attributes:
        id (float): Reminder ID Example: 1.
        completed_at (datetime.datetime): Date of reminder completion Example: 2025-07-01T16:45:55.246Z.
        created_at (datetime.datetime): Reminder created date timestamp Example: 2025-07-01T16:45:55.246Z.
        updated_at (datetime.datetime): Reminder updated date timestamp Example: 2025-07-01T16:45:55.246Z.
        deleted_at (datetime.datetime): Reminder deleted date timestamp Example: 2025-07-01T16:45:55.246Z.
    """

    id: float
    completed_at: datetime.datetime
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        completed_at = self.completed_at.isoformat()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        deleted_at = self.deleted_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "completedAt": completed_at,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "deletedAt": deleted_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        completed_at = isoparse(d.pop("completedAt"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        deleted_at = isoparse(d.pop("deletedAt"))

        reminder_response_public_dto = cls(
            id=id,
            completed_at=completed_at,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
        )

        reminder_response_public_dto.additional_properties = d
        return reminder_response_public_dto

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
