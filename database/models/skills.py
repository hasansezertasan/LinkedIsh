from sqlalchemy import Column, String

from .mixins import TablePlainBase


class Skill(TablePlainBase):
    __tablename__ = "skills"
    name = Column(String(255), nullable=False)

    def __repr__(self):
        return self.name
