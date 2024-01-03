import enum


class AnnouncementCategory(str, enum.Enum):
    EVENT = "EVENT"
    ANNOUNCEMENT = "ANNOUNCEMENT"
    URGENT = "URGENT"
    IMPORTANT = "IMPORTANT"
    INFORMATION = "INFORMATION"
    OTHER = "OTHER"


class FeedbackCategory(str, enum.Enum):
    BUG = "BUG"
    SUGGESTION = "SUGGESTION"
    OTHER = "OTHER"


class FeedbackType(str, enum.Enum):
    MEMBER = "MEMBER"
    ANONYMOUS = "ANONYMOUS"


class UserRole(str, enum.Enum):
    BLOCKED = "BLOCKED"
    USER = "USER"
    ADMIN = "ADMIN"
    SUPERUSER = "SUPERUSER"
