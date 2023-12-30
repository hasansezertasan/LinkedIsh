import datetime

from sqlalchemy import Column, DateTime, Integer

from database.engine import Base


class TablePlainBase(Base):
    __abstract__ = True
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        index=True,
        nullable=False,
        unique=True,
    )
    date_created = Column(DateTime, default=datetime.datetime.utcnow)
    date_updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def __repr__(self):
        return self.id

    def serialize(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
