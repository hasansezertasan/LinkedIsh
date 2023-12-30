from sqlalchemy.orm import Mapped, mapped_column

from ..annotations import String256
from .mixins import TablePlainBase


class Audience(TablePlainBase):
    __tablename__ = "audiences"
    name: Mapped[String256] = mapped_column(unique=True)

    def __repr__(self):
        return self.name
