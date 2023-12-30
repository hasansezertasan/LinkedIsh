from sqlalchemy import Column, ForeignKey, Integer, String, event
from sqlalchemy.orm import relationship

from database.engine import LocalSession

from .mixins import TablePlainBase


class Country(TablePlainBase):
    __tablename__ = "countries"
    name = Column(String(255), nullable=False, unique=True)
    cities = relationship("City", back_populates="country", lazy=False)

    def __repr__(self):
        return self.name


class City(TablePlainBase):
    __tablename__ = "cities"
    name = Column(String(255), nullable=False)
    country_id = Column(Integer, ForeignKey("countries.id"))
    country = relationship("Country", back_populates="cities", lazy=True)

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
