from flask import redirect, url_for
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from sqlalchemy import func

from database.models.mixins import DateDeletedMixin
from database.types import UserRole


class BaseModelView(ModelView):
    """
    - # ! Check the links below and the source code for more information for other great Flask Admin features.
        - [flask_admin.base — flask-admin 1.6.0 documentation](https://flask-admin.readthedocs.io/en/latest/api/mod_base/)
        - [flask_admin.model — flask-admin 1.6.0 documentation](https://flask-admin.readthedocs.io/en/latest/api/mod_model/)
    - # ! Create or select One to One Inline Model
        - [python - flask admin one to one inline_models - Stack Overflow](https://stackoverflow.com/questions/61465038/flask-admin-one-to-one-inline-models)
        - [inline_models don't work for one-to-many · Issue #1405 · flask-admin/flask-admin](https://github.com/flask-admin/flask-admin/issues/1405)
    - # ! Show fields based on the value of another field in flask admin
        - [Show fields based on the value of another field in flask admin - Stack Overflow](https://stackoverflow.com/questions/54383122/show-fields-based-on-the-value-of-another-field-in-flask-admin)
    """

    page_size = 50
    named_filter_urls = True
    column_display_pk = True
    column_display_actions = True
    column_extra_row_actions = None  # ! List of extra row actions, take a look at the docs or source code for more info
    can_export = True
    can_set_page_size = True
    column_display_all_relations = True
    column_auto_select_related = True
    export_types = [
        "csv",
        "json",
        "yaml",
        "xls",
        "xlsx",
        "html",
    ]

    def is_accessible(self):
        return current_user.is_authenticated and current_user.role == UserRole.SUPERUSER

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("account.login"))

    def get_query(self):
        if issubclass(self.model, DateDeletedMixin):
            return self.get_count_query().filter(
                self.model.date_deleted.is_(None),
            )
        return super().get_query()

    def get_count_query(self):
        if issubclass(self.model, DateDeletedMixin):
            return self.session.query(func.count("*")).filter(
                self.model.date_deleted.is_(None),
            )
        return super().get_count_query()

    def is_visible(self) -> bool:
        # Check the docs for more information
        return super().is_visible()

    def is_action_allowed(self, name: str) -> bool:
        # Check the docs for more information
        return super().is_action_allowed(name)

    def is_editable(self, name: str) -> bool:
        # Check the docs for more information
        return super().is_editable(name)

    def _handle_view(self, name, **kwargs):
        # This method will be executed before calling any view method.
        # We can use this to check if the user has permission to access the view or further customize the view like if the time is past midnight we can set `self.can_create = False` etc. Don't forget to call `super()._handle_view(name, **kwargs)` at the end of the method.
        return super()._handle_view(name, **kwargs)
