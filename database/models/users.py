import datetime

from flask_login import UserMixin
from sqlalchemy.orm import Mapped, column_property, mapped_column
from sqlalchemy_file import ImageField
from sqlalchemy_file.validators import ImageValidator, SizeValidator
from sqlalchemy_utils import PasswordType

from database.base import Base

from ..annotations import EmailAddress, PhoneNumber, String128
from ..types import UserRole
from .mixins import DateCreatedMixin, DateUpdatedMixin, IDMixin


class User(Base, IDMixin, DateCreatedMixin, DateUpdatedMixin, UserMixin):
    __tablename__ = "user"
    username: Mapped[String128] = mapped_column(unique=True)
    hashed_password: Mapped[str] = mapped_column(
        PasswordType(
            schemes=[
                "bcrypt",
            ],
            deprecated=[
                "auto",
            ],
        ),
    )
    first_name: Mapped[String128] = mapped_column()
    last_name: Mapped[String128] = mapped_column()
    full_name = column_property(first_name + " " + last_name)
    phone: Mapped[PhoneNumber | None]
    email: Mapped[EmailAddress | None] = mapped_column(
        unique=True,
        index=True,
    )
    birth_date: Mapped[datetime.datetime | None]
    role: Mapped[UserRole] = mapped_column(
        default=UserRole.USER,
    )
    avatar: Mapped[dict | None] = mapped_column(
        type_=ImageField(
            upload_storage="user-avatar",
            multiple=False,
            validators=[
                SizeValidator(max_size="10M"),
            ],
            image_validator=ImageValidator(
                min_wh=(200, 200),
                max_wh=(2000, 2000),
                min_aspect_ratio=1,
                max_aspect_ratio=1,
                allowed_content_types=[
                    "image/jpeg",
                    "image/jpg",
                    "image/png",
                    "image/webp",
                ],
            ),
        )
    )

    def __repr__(self):
        return self.username
