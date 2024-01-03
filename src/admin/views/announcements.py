from wtforms import TextAreaField

from database.models import Announcement
from src.admin.views.mixins import BaseModelView


class AnnouncementModelView(BaseModelView):
    column_list = [
        Announcement.id,
        Announcement.date_created,
        Announcement.date_updated,
        Announcement.title,
        Announcement.category,
        Announcement.url,
    ]
    column_labels = {
        Announcement.id: "ID",
        Announcement.date_created: "Date Created",
        Announcement.date_updated: "Date Updated",
        Announcement.title: "Title",
        Announcement.url: "URL",
    }
    column_searchable_list = [
        Announcement.title,
        Announcement.url,
    ]
    column_sortable_list = [
        Announcement.id,
        Announcement.date_created,
        Announcement.date_updated,
        Announcement.title,
        Announcement.category,
    ]
    column_filters = [
        Announcement.id,
        Announcement.date_created,
        Announcement.date_updated,
        Announcement.title,
    ]
    form_columns = [
        Announcement.title,
        Announcement.content,
        Announcement.category,
        Announcement.url,
    ]
    column_formatters = {
        Announcement.category: lambda v, c, m, p: m.category.value,
        Announcement.url: lambda v, c, m, p: m.url if m.url else "None",
    }
    form_overrides = dict(
        content=TextAreaField,
    )
    can_view_details = True
    details_modal = True
    can_edit = True
    can_create = True
    can_delete = True
    page_size = 50
