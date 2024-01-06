from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database.base import Base

from ..annotations import String256
from .mixins import DateCreatedMixin, DateUpdatedMixin, IDMixin


class School(Base, IDMixin, DateCreatedMixin, DateUpdatedMixin):
    __tablename__ = "school"
    name: Mapped[String256] = mapped_column(unique=True)

    def __repr__(self):
        return self.name


class Field(Base, IDMixin, DateCreatedMixin, DateUpdatedMixin):
    __tablename__ = "field"
    name: Mapped[String256] = mapped_column(unique=True)

    def __repr__(self):
        return self.name


class Degree(Base, IDMixin, DateCreatedMixin, DateUpdatedMixin):
    __tablename__ = "degree"
    name: Mapped[String256] = mapped_column(unique=True)

    def __repr__(self):
        return self.name
