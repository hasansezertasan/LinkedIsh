import datetime

from sqlalchemy.orm import Mapped, mapped_column

from database.engine import Base


class TablePlainBase(Base):
    __abstract__ = True
    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        index=True,
        unique=True,
    )
    date_created: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.utcnow)
    date_updated: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow
    )

    def __repr__(self):
        return self.id

    def serialize(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
