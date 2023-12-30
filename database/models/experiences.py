from sqlalchemy.orm import Mapped, mapped_column

from ..annotations import String256
from .mixins import TablePlainBase


class Company(TablePlainBase):
    __tablename__ = "companies"
    name: Mapped[String256] = mapped_column(unique=True)

    def __repr__(self):
        return self.name


class Position(TablePlainBase):
    __tablename__ = "positions"
    name: Mapped[String256] = mapped_column(unique=True)

    def __repr__(self):
        return self.name
