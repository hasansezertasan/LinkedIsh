from sqlalchemy import TEXT
from sqlalchemy.orm import Mapped, mapped_column

from database.annotations import String256
from database.base import Base
from database.models.mixins import UserCRUDMixin


class TemplateMixin:
    title: Mapped[String256] = mapped_column(
        unique=True,
    )
    description: Mapped[String256]


class EmailTemplate(Base, TemplateMixin, UserCRUDMixin):
    """The email template model."""

    __tablename__ = "template__email"

    subject: Mapped[String256]
    body: Mapped[str] = mapped_column(
        TEXT,
    )
