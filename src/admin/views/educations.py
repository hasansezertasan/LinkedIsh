from database.models import Department, School
from src.admin.views.mixins import BaseModelView


class SchoolModelView(BaseModelView):
    column_list = [
        School.id,
        School.date_created,
        School.date_updated,
        School.name,
    ]
    column_labels = {
        School.id: "ID",
        School.date_created: "Date Created",
        School.date_updated: "Date Updated",
        School.name: "Name",
    }
    column_searchable_list = [
        School.name,
    ]
    column_sortable_list = [
        School.id,
        School.date_created,
        School.date_updated,
        School.name,
    ]
    column_filters = [
        School.id,
        School.date_created,
        School.date_updated,
        School.name,
    ]
    form_columns = [
        School.name,
    ]
    can_view_details = True
    details_modal = True
    can_edit = True
    can_create = True
    can_delete = True
    page_size = 50


class DepartmentModelView(BaseModelView):
    column_list = [
        Department.id,
        Department.date_created,
        Department.date_updated,
        Department.name,
    ]
    column_labels = {
        Department.id: "ID",
        Department.date_created: "Date Created",
        Department.date_updated: "Date Updated",
        Department.name: "Name",
    }
    column_searchable_list = [
        Department.name,
    ]
    column_sortable_list = [
        Department.id,
        Department.date_created,
        Department.date_updated,
        Department.name,
    ]
    column_filters = [
        Department.id,
        Department.date_created,
        Department.date_updated,
        Department.name,
    ]
    form_columns = [
        Department.name,
    ]
    can_view_details = True
    details_modal = True
    can_edit = True
    can_create = True
    can_delete = True
    page_size = 50
