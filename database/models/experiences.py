from sqlalchemy import Column, String

from .mixins import TablePlainBase


class Company(TablePlainBase):
    __tablename__ = "companies"
    name = Column(String(255), nullable=False)

    def __repr__(self):
        return self.name


class Position(TablePlainBase):
    __tablename__ = "positions"
    name = Column(String(255), nullable=False)

    def __repr__(self):
        return self.name
