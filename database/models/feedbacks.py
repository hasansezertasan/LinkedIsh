from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.base import Base
from database.types import FeedbackCategory, FeedbackType

from ..annotations import EmailAddress, String64, String2048
from .mixins import DateCreatedMixin, DateUpdatedMixin, IDMixin, UserCreatedMixin


class Feedback(Base, IDMixin, DateCreatedMixin, DateUpdatedMixin):
    __tablename__ = "feedback"
    subject: Mapped[String64]
    content: Mapped[String2048]
    category: Mapped[FeedbackCategory] = mapped_column()
    type: Mapped[FeedbackType] = mapped_column()

    __mapper_args__ = {
        "polymorphic_identity": "plain",
        "polymorphic_on": type,
    }

    def __repr__(self):
        return self.subject


class MemberFeedback(Feedback, UserCreatedMixin):
    __tablename__ = "feedback__member"
    id: Mapped[int] = mapped_column(
        ForeignKey("feedback.id"),
        name="id",
        primary_key=True,
    )

    __mapper_args__ = {
        "polymorphic_identity": "MEMBER",
    }


class AnonymousFeedback(Feedback):
    __tablename__ = "feedback__anonymous"
    id: Mapped[int] = mapped_column(
        ForeignKey("feedback.id"),
        name="id",
        primary_key=True,
    )
    email: Mapped[EmailAddress]

    __mapper_args__ = {
        "polymorphic_identity": "ANONYMOUS",
    }
