from sqlalchemy.orm import Mapped, mapped_column

from database.base import Base

from ..annotations import String256
from .mixins import TablePlainBase


class Company(Base, TablePlainBase):
    __tablename__ = "companies"
    name: Mapped[String256] = mapped_column(unique=True)

    def __repr__(self):
        return self.name


class Position(Base, TablePlainBase):
    __tablename__ = "positions"
    name: Mapped[String256] = mapped_column(unique=True)

    def __repr__(self):
        return self.name
