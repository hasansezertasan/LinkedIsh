from sqlalchemy import Column, String

from .mixins import TablePlainBase


class School(TablePlainBase):
    __tablename__ = "schools"
    name = Column(String(255), nullable=False)

    def __repr__(self):
        return self.name


class Department(TablePlainBase):
    __tablename__ = "departments"
    name = Column(String(255), nullable=False)

    def __repr__(self):
        return self.name
