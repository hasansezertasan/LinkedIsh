from flask_ckeditor import CKEditorField

from database.models import EmailTemplate
from src.admin.views.mixins import BaseModelView


class EmailTemplateModelView(BaseModelView):
    create_template = "/edit.html"
    edit_template = "/edit.html"
    column_list = [
        EmailTemplate.id,
        EmailTemplate.date_created,
        EmailTemplate.date_updated,
        EmailTemplate.title,
        EmailTemplate.description,
    ]
    column_details_list = [
        EmailTemplate.id,
        EmailTemplate.date_created,
        EmailTemplate.date_updated,
        EmailTemplate.title,
        EmailTemplate.description,
        EmailTemplate.subject,
        EmailTemplate.body,
    ]
    column_labels = {
        EmailTemplate.id: "ID",
        EmailTemplate.date_created: "Date Created",
        EmailTemplate.date_updated: "Date Updated",
        EmailTemplate.title: "Title",
        EmailTemplate.description: "Description",
        EmailTemplate.subject: "Subject",
        EmailTemplate.body: "Body",
    }
    column_searchable_list = [
        EmailTemplate.title,
        EmailTemplate.description,
        EmailTemplate.subject,
    ]
    column_sortable_list = [
        EmailTemplate.id,
        EmailTemplate.date_created,
        EmailTemplate.date_updated,
        EmailTemplate.title,
    ]
    column_filters = [
        EmailTemplate.id,
        EmailTemplate.date_created,
        EmailTemplate.date_updated,
        EmailTemplate.title,
        EmailTemplate.description,
        EmailTemplate.subject,
    ]
    form_columns = [
        EmailTemplate.title,
        EmailTemplate.description,
        EmailTemplate.subject,
        EmailTemplate.body,
    ]
    form_overrides = dict(
        body=CKEditorField,
    )
    can_view_details = True
    details_modal = True
    can_edit = True
    can_create = True
    can_delete = True
    page_size = 50
