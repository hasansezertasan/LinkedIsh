from wtforms import TextAreaField

from database.models import AnonymousFeedback, Feedback, MemberFeedback
from database.types import FeedbackCategory, FeedbackType
from src.admin.views.mixins import BaseModelView


class FeedbackModelView(BaseModelView):
    column_list = [
        Feedback.id,
        Feedback.date_created,
        Feedback.date_updated,
        Feedback.subject,
        Feedback.category,
        Feedback.type,
    ]
    column_labels = {
        "id": "ID",
        Feedback.date_created: "Date Created",
        Feedback.date_updated: "Date Updated",
        Feedback.subject: "Title",
        Feedback.content: "Content",
        Feedback.category: "Category",
        Feedback.type: "Type",
    }
    column_searchable_list = [
        Feedback.subject,
        Feedback.content,
        Feedback.category,
        Feedback.type,
    ]
    column_sortable_list = [
        "id",
        Feedback.date_created,
        Feedback.date_updated,
        Feedback.subject,
        Feedback.category,
        Feedback.type,
    ]
    column_filters = [
        "id",
        Feedback.date_created,
        Feedback.date_updated,
        Feedback.subject,
        Feedback.category,
        Feedback.type,
    ]
    column_formatters = {
        Feedback.category: lambda v, c, m, p: m.category.value,
    }
    form_columns = [
        Feedback.subject,
        Feedback.content,
        Feedback.category,
        Feedback.type,
        Feedback.is_read,
    ]
    form_overrides = dict(
        content=TextAreaField,
    )
    form_args = {
        "is_read": {
            "coerce": int,
        },
    }
    column_choices = {
        "is_read": [
            (True, "Read"),
            (False, "Not Read"),
        ],
        "type": [
            (FeedbackType.MEMBER.value, "Member"),
            (FeedbackType.ANONYMOUS.value, "Anonymous"),
        ],
        "category": [
            (FeedbackCategory.SUGGESTION, "Suggestion"),
            (FeedbackCategory.BUG, "Bug"),
            (FeedbackCategory.OTHER, "Other"),
        ],
    }
    form_choices = {
        "is_read": [
            (1, "Read"),
            (0, "Not Read"),
        ],
    }
    can_view_details = True
    details_modal = True
    can_edit = False
    can_create = False
    can_delete = False
    page_size = 50


class MemberFeedbackView(BaseModelView):
    column_list = [
        "id",
        MemberFeedback.date_created,
        MemberFeedback.date_updated,
        MemberFeedback.subject,
        MemberFeedback.category,
        "user",
    ]
    column_labels = {
        "id": "ID",
        MemberFeedback.date_created: "Date Created",
        MemberFeedback.date_updated: "Date Updated",
        MemberFeedback.subject: "Title",
        MemberFeedback.content: "Content",
        MemberFeedback.category: "Category",
        "user": "User",
    }
    column_searchable_list = [
        MemberFeedback.subject,
        MemberFeedback.content,
        MemberFeedback.category,
    ]
    column_sortable_list = [
        "id",
        MemberFeedback.date_created,
        MemberFeedback.date_updated,
        MemberFeedback.subject,
        MemberFeedback.category,
        "user",
    ]
    column_filters = [
        MemberFeedback.date_created,
        MemberFeedback.date_updated,
        MemberFeedback.subject,
        MemberFeedback.category,
        "user",
    ]
    form_columns = [
        MemberFeedback.subject,
        MemberFeedback.content,
        MemberFeedback.category,
    ]
    column_formatters = {
        MemberFeedback.category: lambda v, c, m, p: m.category.value,
    }
    can_view_details = True
    details_modal = True
    can_edit = True
    can_create = False
    can_delete = False
    page_size = 50


class AnonymousFeedbackView(BaseModelView):
    column_list = [
        "id",
        AnonymousFeedback.date_created,
        AnonymousFeedback.date_updated,
        AnonymousFeedback.subject,
        AnonymousFeedback.category,
        AnonymousFeedback.email,
    ]
    column_labels = {
        "id": "ID",
        AnonymousFeedback.date_created: "Date Created",
        AnonymousFeedback.date_updated: "Date Updated",
        AnonymousFeedback.subject: "Title",
        AnonymousFeedback.content: "Content",
        AnonymousFeedback.category: "Category",
        AnonymousFeedback.email: "Email",
    }
    column_searchable_list = [
        AnonymousFeedback.subject,
        AnonymousFeedback.content,
        AnonymousFeedback.category,
        AnonymousFeedback.email,
    ]
    column_sortable_list = [
        "id",
        AnonymousFeedback.date_created,
        AnonymousFeedback.date_updated,
        AnonymousFeedback.subject,
        AnonymousFeedback.category,
        AnonymousFeedback.email,
    ]
    column_filters = [
        AnonymousFeedback.date_created,
        AnonymousFeedback.date_updated,
        AnonymousFeedback.subject,
        AnonymousFeedback.category,
        AnonymousFeedback.email,
    ]
    form_columns = [
        AnonymousFeedback.subject,
        AnonymousFeedback.content,
        AnonymousFeedback.category,
        AnonymousFeedback.email,
    ]
    column_formatters = {
        AnonymousFeedback.category: lambda v, c, m, p: m.category.value,
    }
    form_overrides = dict(
        content=TextAreaField,
    )
    can_view_details = True
    details_modal = True
    can_edit = True
    can_create = False
    can_delete = False
    page_size = 50
