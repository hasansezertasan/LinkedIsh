import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship


class ActiveMixin:
    is_active: Mapped[bool] = mapped_column(
        name="is_active",
        default=True,
        sort_order=-2,
    )
    """Indicates if the record is active or not."""


class CorrectMixin:
    is_correct: Mapped[bool] = mapped_column(
        name="is_correct",
        default=False,
        sort_order=-2,
    )
    """Indicates if the record is correct."""


class IDMixin:
    """Base class for tables with id."""

    id: Mapped[int] = mapped_column(
        name="id",
        primary_key=True,
        autoincrement=True,
        index=True,
        unique=True,
        sort_order=-2,
    )
    """Identifier of the record."""

    def __repr__(self):
        return f"{self.id}" if hasattr(self, "id") else self.__class__.__name__


class DateCreatedMixin:
    """Base class for tables with date_created column and serialize method."""

    date_created: Mapped[datetime.datetime] = mapped_column(
        name="date_created",
        default=datetime.datetime.utcnow,
        index=True,
        sort_order=-2,
    )
    """Date when the record was created."""


class DateUpdatedMixin:
    """Base class for tables with date_updated column and serialize method."""

    date_updated: Mapped[datetime.datetime] = mapped_column(
        name="date_updated",
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        index=True,
        sort_order=-2,
    )
    """Date when the record was updated."""


class DateDeletedMixin:
    """Base class for tables with date_deleted column and serialize method."""

    date_deleted: Mapped[datetime.datetime | None] = mapped_column(
        name="date_deleted",
        default=None,
        index=True,
        sort_order=-2,
    )
    """Date when the record was deleted. """


class DateCRUDMixin(DateCreatedMixin, DateUpdatedMixin, DateDeletedMixin):
    """Base class for tables with date_created and date_updated columns and serialize method."""


class UserDeletedMixin:
    """Base class for tables with user_deleted column and serialize method."""

    @declared_attr
    def deleted_by_user_id(cls) -> Mapped[int | None]:
        """User who deleted the record."""
        return mapped_column(
            ForeignKey("user.id"),
            sort_order=-1,
        )

    @declared_attr
    def deleted_by_user(cls) -> Mapped["User"]:
        """User who deleted the record."""
        return relationship(
            "User",
            foreign_keys=[cls.deleted_by_user_id],
        )


class UserUpdatedMixin:
    """Base class for tables with user_updated column and serialize method."""

    @declared_attr
    def updated_by_user_id(cls) -> Mapped[int | None]:
        """User who updated the record."""
        return mapped_column(
            ForeignKey("user.id"),
            sort_order=-1,
        )

    @declared_attr
    def updated_by_user(cls) -> Mapped["User"]:
        """User who updated the record."""
        return relationship(
            "User",
            foreign_keys=[cls.updated_by_user_id],
        )


class UserCreatedMixin:
    """Base class for tables with user_created column and serialize method."""

    @declared_attr
    def user_id(cls) -> Mapped[int | None]:
        """User who created the record."""
        return mapped_column(
            ForeignKey("user.id"),
            sort_order=-1,
        )

    @declared_attr
    def user(cls) -> Mapped["User"]:
        """User who created the record."""
        return relationship(
            "User",
            foreign_keys=[cls.user_id],
        )


class DeleteMixin(UserDeletedMixin, DateDeletedMixin):
    """Base class for delete operations."""


class UpdateMixin(UserUpdatedMixin, DateUpdatedMixin):
    """Base class for update operations."""


class CreateMixin(UserCreatedMixin, DateCreatedMixin):
    """Base class for create operations."""


class ReadMixin:
    """Base class for read operations."""


class UserCRUDMixin(ReadMixin, IDMixin, CreateMixin, UpdateMixin, DeleteMixin):
    """Base class for CRUD operations."""
