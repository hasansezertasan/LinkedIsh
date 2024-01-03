from database.models import Company, Position
from src.admin.views.mixins import BaseModelView


class CompanyModelView(BaseModelView):
    column_list = [
        Company.id,
        Company.date_created,
        Company.date_updated,
        Company.name,
    ]
    column_labels = {
        Company.id: "ID",
        Company.date_created: "Date Created",
        Company.date_updated: "Date Updated",
        Company.name: "Name",
    }
    column_searchable_list = [
        Company.name,
    ]
    column_sortable_list = [
        Company.id,
        Company.date_created,
        Company.date_updated,
        Company.name,
    ]
    column_filters = [
        Company.id,
        Company.date_created,
        Company.date_updated,
        Company.name,
    ]
    form_columns = [
        Company.name,
    ]
    can_view_details = True
    details_modal = True
    can_edit = True
    can_create = True
    can_delete = True
    page_size = 50


class PositionModelView(BaseModelView):
    column_list = [
        Position.id,
        Position.date_created,
        Position.date_updated,
        Position.name,
    ]
    column_labels = {
        Position.id: "ID",
        Position.date_created: "Date Created",
        Position.date_updated: "Date Updated",
        Position.name: "Name",
    }
    column_searchable_list = [
        Position.name,
    ]
    column_sortable_list = [
        Position.id,
        Position.date_created,
        Position.date_updated,
        Position.name,
    ]
    column_filters = [
        Position.id,
        Position.date_created,
        Position.date_updated,
        Position.name,
    ]
    form_columns = [
        Position.name,
    ]
    can_view_details = True
    details_modal = True
    can_edit = True
    can_create = True
    can_delete = True
    page_size = 50
