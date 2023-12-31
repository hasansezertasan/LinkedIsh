from flask import redirect, url_for
from flask_admin import AdminIndexView, BaseView, expose
from flask_login import current_user

from database.types import UserRole


class PingView(BaseView):
    @expose("/")
    def ping(self):
        return "Pong!"


class IndexView(AdminIndexView):
    @expose(url="/", methods=["GET"])
    def root(self):
        return self.render("index.html")

    def is_accessible(self):
        return current_user.is_authenticated and current_user.role == UserRole.SUPERUSER

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("account.login"))
