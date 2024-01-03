from sqlalchemy.orm import Mapped

from database.base import Base
from database.types import AnnouncementCategory

from ..annotations import URL, String64, String1024
from .mixins import UserCRUDMixin


class Announcement(Base, UserCRUDMixin):
    __tablename__ = "announcement"
    title: Mapped[String64]
    content: Mapped[String1024]
    category: Mapped[AnnouncementCategory]
    url: Mapped[URL | None]

    def __repr__(self):
        return self.title
