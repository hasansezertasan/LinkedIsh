from sqlalchemy import Column, String

from .mixins import TablePlainBase


class Language(TablePlainBase):
    __tablename__ = "languages"
    name = Column(String(255), nullable=False)

    def __repr__(self):
        return self.name
