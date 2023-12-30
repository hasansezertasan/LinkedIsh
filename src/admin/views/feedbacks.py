from wtforms import TextAreaField

from database.models import Feedback
from src.admin.views.mixins import BaseModelView


class FeedbackModelView(BaseModelView):
    columns_list = [
        Feedback.id,
        Feedback.date_created,
        Feedback.date_updated,
        Feedback.subject,
        Feedback.category,
    ]
    column_labels = {
        Feedback.id: "ID",
        Feedback.date_created: "Date Created",
        Feedback.date_updated: "Date Updated",
        Feedback.subject: "Title",
    }
    column_searchable_list = [
        Feedback.subject,
    ]
    column_sortable_list = [
        Feedback.id,
        Feedback.date_created,
        Feedback.date_updated,
        Feedback.subject,
        Feedback.category,
    ]
    column_filters = [
        Feedback.id,
        Feedback.date_created,
        Feedback.date_updated,
        Feedback.subject,
    ]
    form_columns = [
        Feedback.subject,
        Feedback.content,
    ]
    column_formatters = {
        Feedback.category: lambda v, c, m, p: m.category.value,
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
