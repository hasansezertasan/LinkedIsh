from sqlalchemy.orm import Mapped

from database.types import FeedbackCategory

from ..annotations import String64, String2048
from .mixins import TablePlainBase


class Feedback(TablePlainBase):
    __tablename__ = "feedbacks"
    subject: Mapped[String64]
    content: Mapped[String2048]
    category: Mapped[FeedbackCategory]

    def __repr__(self):
        return self.subject
