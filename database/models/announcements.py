from sqlalchemy import Column, Enum, String

from database.types import AnnouncementCategory

from .mixins import TablePlainBase


class Announcement(TablePlainBase):
    __tablename__ = "announcements"
    # ! user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String(100), nullable=False)
    content = Column(String(1500), nullable=False)
    category = Column(Enum(AnnouncementCategory), nullable=False)
    url = Column(String(250))

    def __repr__(self):
        return self.title
