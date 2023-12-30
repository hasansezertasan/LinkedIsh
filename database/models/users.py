from flask_login import UserMixin
from sqlalchemy import Column, Enum, String, event
from werkzeug.security import check_password_hash, generate_password_hash

from .mixins import TablePlainBase


class User(TablePlainBase, UserMixin):
    __tablename__ = "users"
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
    surname = Column(String(100), nullable=False)

    email = Column(String(100), nullable=False, unique=True)
    role = Column(Enum("user", "admin"), default="user")

    def __repr__(self):
        return self.username

    def verify_password(self, password):
        return check_password_hash(self.password, password)


@event.listens_for(User.password, "set", retval=True)
def hash_user_password(target, value, oldvalue, initiator):
    if value != oldvalue:
        return generate_password_hash(value)
    return value
