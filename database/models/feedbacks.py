from sqlalchemy import Column, Enum, String

from database.types import FeedbackCategory

from .mixins import TablePlainBase


class Feedback(TablePlainBase):
    __tablename__ = "feedbacks"
    # ! user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    subject = Column(String(50), nullable=False)
    content = Column(String(1500), nullable=False)
    category = Column(Enum(FeedbackCategory), nullable=False)

    def __repr__(self):
        return self.subject
