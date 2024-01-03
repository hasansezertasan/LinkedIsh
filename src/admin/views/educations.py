from database.models import School, SchoolDepartment
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


class SchoolDepartmentModelView(BaseModelView):
    column_list = [
        SchoolDepartment.id,
        SchoolDepartment.date_created,
        SchoolDepartment.date_updated,
        SchoolDepartment.name,
    ]
    column_labels = {
        SchoolDepartment.id: "ID",
        SchoolDepartment.date_created: "Date Created",
        SchoolDepartment.date_updated: "Date Updated",
        SchoolDepartment.name: "Name",
    }
    column_searchable_list = [
        SchoolDepartment.name,
    ]
    column_sortable_list = [
        SchoolDepartment.id,
        SchoolDepartment.date_created,
        SchoolDepartment.date_updated,
        SchoolDepartment.name,
    ]
    column_filters = [
        SchoolDepartment.id,
        SchoolDepartment.date_created,
        SchoolDepartment.date_updated,
        SchoolDepartment.name,
    ]
    form_columns = [
        SchoolDepartment.name,
    ]
    can_view_details = True
    details_modal = True
    can_edit = True
    can_create = True
    can_delete = True
    page_size = 50
