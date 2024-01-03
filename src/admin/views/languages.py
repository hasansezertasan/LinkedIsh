from database.models import Language
from src.admin.views.mixins import BaseModelView


class LanguageModelView(BaseModelView):
    column_list = [
        Language.id,
        Language.date_created,
        Language.date_updated,
        Language.name,
    ]
    column_labels = {
        Language.id: "ID",
        Language.date_created: "Date Created",
        Language.date_updated: "Date Updated",
        Language.name: "Name",
    }
    column_searchable_list = [
        Language.name,
    ]
    column_sortable_list = [
        Language.id,
        Language.date_created,
        Language.date_updated,
        Language.name,
    ]
    column_filters = [
        Language.id,
        Language.date_created,
        Language.date_updated,
        Language.name,
    ]
    form_columns = [
        Language.name,
    ]
    can_view_details = True
    details_modal = True
    can_edit = True
    can_create = True
    can_delete = True
    page_size = 50
