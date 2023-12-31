from sqlalchemy.orm import Mapped

from database.base import Base
from database.types import AnnouncementCategory

from ..annotations import URL, String64, String1024
from .mixins import DateCreatedMixin, DateUpdatedMixin, IDMixin


class Announcement(Base, IDMixin, DateCreatedMixin, DateUpdatedMixin):
    __tablename__ = "announcements"
    title: Mapped[String64]
    content: Mapped[String1024]
    category: Mapped[AnnouncementCategory]
    url: Mapped[URL]

    def __repr__(self):
        return self.title
