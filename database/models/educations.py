from sqlalchemy.orm import Mapped, mapped_column

from ..annotations import String256
from .mixins import TablePlainBase


class School(TablePlainBase):
    __tablename__ = "schools"
    name: Mapped[String256] = mapped_column(unique=True)

    def __repr__(self):
        return self.name


class Department(TablePlainBase):
    __tablename__ = "departments"
    name: Mapped[String256] = mapped_column(unique=True)

    def __repr__(self):
        return self.name
