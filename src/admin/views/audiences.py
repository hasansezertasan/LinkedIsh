from database.models import Audience
from src.admin.views.mixins import BaseModelView


class AudienceModelView(BaseModelView):
    columns_list = [
        Audience.id,
        Audience.date_created,
        Audience.date_updated,
        Audience.name,
    ]
    column_labels = {
        Audience.id: "ID",
        Audience.date_created: "Date Created",
        Audience.date_updated: "Date Updated",
        Audience.name: "Name",
    }
    column_searchable_list = [
        Audience.name,
    ]
    column_sortable_list = [
        Audience.id,
        Audience.date_created,
        Audience.date_updated,
        Audience.name,
    ]
    column_filters = [
        Audience.id,
        Audience.date_created,
        Audience.date_updated,
        Audience.name,
    ]
    form_columns = [
        Audience.name,
    ]
    can_view_details = True
    details_modal = True
    can_edit = True
    can_create = True
    can_delete = True
    page_size = 50
