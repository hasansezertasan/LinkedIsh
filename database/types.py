import enum


class AnnouncementCategory(enum.Enum):
    event = "Event"
    announcement = "Announcement"
    urgent = "Urgent"
    important = "Important"
    information = "Information"
    other = "Other"


class FeedbackCategory(enum.Enum):
    bug = "Bug"
    suggestion = "Suggestion"
    other = "Other"
