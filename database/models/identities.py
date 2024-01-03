from sqlalchemy.orm import Mapped

from database.annotations import EmailAddress, PhoneNumber
from database.base import Base
from database.models.mixins import CreateMixin, IDMixin


class EmailID(Base, IDMixin, CreateMixin):
    __tablename__ = "identity__email"
    address: Mapped[EmailAddress]


class PhoneID(Base, IDMixin, CreateMixin):
    __tablename__ = "identity__phone"
    address: Mapped[PhoneNumber]
