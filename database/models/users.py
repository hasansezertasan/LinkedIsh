from flask_login import UserMixin
from sqlalchemy import event
from sqlalchemy.orm import Mapped, mapped_column
from werkzeug.security import check_password_hash, generate_password_hash

from database.base import Base

from ..annotations import EmailAddress, String128
from ..types import UserRole
from .mixins import TablePlainBase


class User(Base, TablePlainBase, UserMixin):
    __tablename__ = "users"
    username: Mapped[String128] = mapped_column(unique=True)
    password: Mapped[String128]
    name: Mapped[String128]
    surname: Mapped[String128]

    email: Mapped[EmailAddress] = mapped_column(unique=True)
    role: Mapped[UserRole] = mapped_column(default=UserRole.USER)

    def __repr__(self):
        return self.username

    def verify_password(self, password):
        return check_password_hash(self.password, password)


@event.listens_for(User.password, "set", retval=True)
def hash_user_password(target, value, oldvalue, initiator):
    if value != oldvalue:
        return generate_password_hash(value)
    return value
