from flask import redirect, url_for
from flask_admin import AdminIndexView, BaseView, expose
from flask_login import current_user


class PingView(BaseView):
    @expose("/")
    def ping(self):
        return "Pong!"


class IndexView(AdminIndexView):
    @expose(url="/", methods=["GET"])
    def root(self):
        return self.render("index.html")

    def is_accessible(self):
        return current_user.is_authenticated and current_user.role == "admin"

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("user.login"))
