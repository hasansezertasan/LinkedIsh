from typing import Annotated

from sqlalchemy import DECIMAL, String, Unicode
from sqlalchemy.orm import mapped_column
from sqlalchemy_utils import EmailType, IPAddressType, PhoneNumberType, URLType

PostalCode = Annotated[
    str,
    mapped_column(
        type_=String(5),
        info={
            "label": "Postal Code",
            "description": "The postal code of the address.",
            "example": "12345",
        },
    ),
]
Latitude = Annotated[
    float,
    mapped_column(
        type_=DECIMAL(precision=10, scale=8),
    ),
]
Longitude = Annotated[
    float,
    mapped_column(
        type_=DECIMAL(precision=11, scale=8),
    ),
]
Money = Annotated[
    float,
    mapped_column(
        type_=DECIMAL(precision=18, scale=9),
    ),
]
PhoneNumber = Annotated[
    str,
    mapped_column(
        type_=Unicode(64),
    ),
]
EmailAddress = Annotated[
    str,
    mapped_column(type_=EmailType),
]
String64 = Annotated[
    str,
    mapped_column(
        type_=String(64),
    ),
]
String128 = Annotated[
    str,
    mapped_column(
        type_=String(128),
    ),
]
String256 = Annotated[
    str,
    mapped_column(
        type_=String(256),
    ),
]
String512 = Annotated[
    str,
    mapped_column(
        type_=String(512),
    ),
]
String1024 = Annotated[
    str,
    mapped_column(
        type_=String(1024),
    ),
]
String2048 = Annotated[
    str,
    mapped_column(
        type_=String(2048),
    ),
]
UUIDString = Annotated[
    str,
    mapped_column(
        type_=String(36),
    ),
]
IPAddress = Annotated[
    str,
    mapped_column(
        type_=IPAddressType(64),
    ),
]
URL = Annotated[
    str,
    mapped_column(
        type_=URLType,
    ),
]
