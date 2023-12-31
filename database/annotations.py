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
            "description": "The postal code of the record.",
            "example": "12345",
        },
    ),
]
Latitude = Annotated[
    float,
    mapped_column(
        type_=DECIMAL(precision=10, scale=8),
        info={
            "label": "Latitude",
            "description": "The latitude of the record.",
            "example": "37.7749",
        },
    ),
]
Longitude = Annotated[
    float,
    mapped_column(
        type_=DECIMAL(precision=11, scale=8),
        info={
            "label": "Longitude",
            "description": "The longitude of the record.",
            "example": "-122.4194",
        },
    ),
]
Money = Annotated[
    float,
    mapped_column(
        type_=DECIMAL(precision=18, scale=9),
        info={
            "label": "Money",
            "description": "The amount of money.",
            "example": "123.45",
        },
    ),
]
PhoneNumber = Annotated[
    str,
    mapped_column(
        type_=Unicode(64),
        info={
            "label": "Phone Number",
            "description": "The phone number of the record.",
            "example": "+1 (234) 567-8900",
        },
    ),
]
EmailAddress = Annotated[
    str,
    mapped_column(
        type_=EmailType,
        info={
            "label": "Email Address",
            "description": "The email address of the record.",
            "example": "john@doe.com",
        },
    ),
]
String64 = Annotated[
    str,
    mapped_column(
        type_=String(64),
        info={
            "label": "String 64",
            "description": "A string with a maximum length of 64 characters.",
            "example": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        },
    ),
]
String128 = Annotated[
    str,
    mapped_column(
        type_=String(128),
        info={
            "label": "String 128",
            "description": "A string with a maximum length of 128 characters.",
            "example": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        },
    ),
]
String256 = Annotated[
    str,
    mapped_column(
        type_=String(256),
        info={
            "label": "String 256",
            "description": "A string with a maximum length of 256 characters.",
            "example": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        },
    ),
]
String512 = Annotated[
    str,
    mapped_column(
        type_=String(512),
        info={
            "label": "String 512",
            "description": "A string with a maximum length of 512 characters.",
            "example": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        },
    ),
]
String1024 = Annotated[
    str,
    mapped_column(
        type_=String(1024),
        info={
            "label": "String 1024",
            "description": "A string with a maximum length of 1024 characters.",
            "example": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        },
    ),
]
String2048 = Annotated[
    str,
    mapped_column(
        type_=String(2048),
        info={
            "label": "String 2048",
            "description": "A string with a maximum length of 2048 characters.",
            "example": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        },
    ),
]
UUIDString = Annotated[
    str,
    mapped_column(
        type_=String(36),
        info={
            "label": "UUID String",
            "description": "A UUID string.",
            "example": "123e4567-e89b-12d3-a456-426614174000",
        },
    ),
]
IPAddress = Annotated[
    str,
    mapped_column(
        type_=IPAddressType(64),
        info={
            "label": "IP Address",
            "description": "The IP address of the record.",
            "example": "0.0.0.0",
        },
    ),
]
URL = Annotated[
    str,
    mapped_column(
        type_=URLType,
        info={
            "label": "URL",
            "description": "The URL of the record.",
            "example": "https://example.com",
        },
    ),
]
