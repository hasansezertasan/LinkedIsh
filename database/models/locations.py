from sqlalchemy import ForeignKey, event
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.engine import LocalSession

from ..annotations import String256
from .mixins import TablePlainBase


class Country(TablePlainBase):
    __tablename__ = "countries"
    name: Mapped[String256] = mapped_column(unique=True)
    cities: Mapped["City"] = relationship(back_populates="country")

    def __repr__(self):
        return self.name


class City(TablePlainBase):
    __tablename__ = "cities"
    name: Mapped[String256] = mapped_column(unique=True)
    country_id: Mapped[int] = mapped_column(ForeignKey("countries.id"))
    country: Mapped["Country"] = relationship(back_populates="cities")

    def __repr__(self):
        return self.name


# Remove cities when country is deleted
@event.listens_for(Country, "after_delete")
def receive_after_delete(mapper, connection, target):
    # ! Test this one.
    with LocalSession() as db:
        cities = db.query(City).filter(City.country_id == target.id).all()
        for city in cities:
            db.delete(city)
        db.commit()
    # Or This
    # connection.execute(City.__table__.delete().where(City.country_id == target.id))
