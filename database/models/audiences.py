from sqlalchemy import Column, String

from .mixins import TablePlainBase


class Audience(TablePlainBase):
    __tablename__ = "audiences"
    name = Column(String(255), nullable=False)

    def __repr__(self):
        return self.name
