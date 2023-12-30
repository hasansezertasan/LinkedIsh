import enum


class AnnouncementCategory(str, enum.Enum):
    event = "Event"
    announcement = "Announcement"
    urgent = "Urgent"
    important = "Important"
    information = "Information"
    other = "Other"


class FeedbackCategory(str, enum.Enum):
    bug = "Bug"
    suggestion = "Suggestion"
    other = "Other"


class UserRole(str, enum.Enum):
    BLOCKED = "BLOCKED"
    USER = "USER"
    ADMIN = "ADMIN"
    SUPERUSER = "SUPERUSER"
