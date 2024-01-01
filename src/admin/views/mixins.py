from flask import redirect, url_for
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

from database.types import UserRole


class BaseModelView(ModelView):
    page_size = 50

    def is_accessible(self):
        return current_user.is_authenticated and current_user.role == UserRole.SUPERUSER

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("account.login"))
