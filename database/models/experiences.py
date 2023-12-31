from sqlalchemy.orm import Mapped, mapped_column

from database.base import Base

from ..annotations import String256
from .mixins import DateCreatedMixin, DateUpdatedMixin, IDMixin


class Company(Base, IDMixin, DateCreatedMixin, DateUpdatedMixin):
    __tablename__ = "company"
    name: Mapped[String256] = mapped_column(unique=True)

    def __repr__(self):
        return self.name


class CompanyDepartment(Base, IDMixin, DateCreatedMixin, DateUpdatedMixin):
    __tablename__ = "company__department"
    name: Mapped[String256] = mapped_column(unique=True)

    def __repr__(self):
        return self.name


class Organization(Base, IDMixin, DateCreatedMixin, DateUpdatedMixin):
    __tablename__ = "organization"
    name: Mapped[String256] = mapped_column(unique=True)

    def __repr__(self):
        return self.name


class Industry(Base, IDMixin, DateCreatedMixin, DateUpdatedMixin):
    __tablename__ = "industry"
    name: Mapped[String256] = mapped_column(unique=True)

    def __repr__(self):
        return self.name
