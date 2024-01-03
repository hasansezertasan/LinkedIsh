from database.models import Company, CompanyDepartment
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


class CompanyDepartmentModelView(BaseModelView):
    column_list = [
        CompanyDepartment.id,
        CompanyDepartment.date_created,
        CompanyDepartment.date_updated,
        CompanyDepartment.name,
    ]
    column_labels = {
        CompanyDepartment.id: "ID",
        CompanyDepartment.date_created: "Date Created",
        CompanyDepartment.date_updated: "Date Updated",
        CompanyDepartment.name: "Name",
    }
    column_searchable_list = [
        CompanyDepartment.name,
    ]
    column_sortable_list = [
        CompanyDepartment.id,
        CompanyDepartment.date_created,
        CompanyDepartment.date_updated,
        CompanyDepartment.name,
    ]
    column_filters = [
        CompanyDepartment.id,
        CompanyDepartment.date_created,
        CompanyDepartment.date_updated,
        CompanyDepartment.name,
    ]
    form_columns = [
        CompanyDepartment.name,
    ]
    can_view_details = True
    details_modal = True
    can_edit = True
    can_create = True
    can_delete = True
    page_size = 50
