from flask import flash, redirect, url_for
from flask_admin import expose
from flask_admin.model.template import EndpointLinkRowAction, LinkRowAction, TemplateLinkRowAction
from markupsafe import Markup
from wtforms import validators

from database.models import User
from database.types import UserRole
from src.admin.views.mixins import BaseModelView


class UserModelView(BaseModelView):
    column_list = [
        "id",
        "username",
        "first_name",
        "last_name",
        "role",
    ]
    column_details_list = [
        "id",
        "date_created",
        "date_updated",
        "username",
        "first_name",
        "last_name",
        "role",
    ]
    column_labels = {
        "id": "ID",
        "date_created": "Created",
        "date_updated": "Updated",
        "username": "Username",
        "hashed_password": "Password",
        "first_name": "First Name",
        "last_name": "Last Name",
        "role": "Role",
    }
    column_descriptions = {
        "id": "User ID",
        "date_created": "The date the user was created",
        "date_updated": "The date the user was updated",
        "username": "The username of the user",
        "first_name": "First Name",
        "last_name": "Last Name",
        "hashed_password": "The password of the user",
        "role": "The role of the user",
    }
    column_filters = [
        "id",
        "date_created",
        "date_updated",
        "username",
        "first_name",
        "last_name",
        "email",
        "role",
    ]
    column_formatters = {
        "full_name": lambda v, c, m, p: f"{m.first_name} {m.last_name}",
        "dates": lambda v, c, m, p: Markup(f"Created:{m.date_created}<br>Updated: {m.date_updated}"),
        "contact": lambda v, c, m, p: Markup(f"Email: {m.email}<br>Phone: {m.phone}"),
    }
    column_choices = {
        "role": [
            (UserRole.SUPERUSER, "Super User"),
            (UserRole.ADMIN, "Admin"),
            (UserRole.USER, "User"),
            (UserRole.BLOCKED, "Blocked"),
        ],
    }
    form_choices = {
        "role": [
            ("SUPERUSER", "Super User"),
            ("ADMIN", "Admin"),
            ("USER", "User"),
            ("BLOCKED", "Blocked"),
        ],
    }
    form_excluded_columns = [
        "date_created",
        "date_updated",
        "hashed_password",
    ]
    form_args = {
        "username": {
            "label": "Username",
            "validators": [
                validators.DataRequired(),
                validators.Length(min=8, max=255),
            ],
        },
        "password": {
            "label": "Password",
            "validators": [
                validators.DataRequired(),
                validators.Length(min=8, max=255),
            ],
        },
        "first_name": {
            "label": "First Name",
        },
        "last_name": {
            "label": "Last Name",
        },
        "email": {"label": "Email"},
        "role": {
            "label": "Role",
        },
    }
    form_widget_args = {
        "date_created": {
            "disabled": True,
        },
        "date_updated": {
            "disabled": True,
        },
        "username": {
            "placeholder": "Username",
        },
        "password": {
            "placeholder": "Password",
        },
        "first_name": {
            "placeholder": "First Name",
        },
        "last_name": {
            "placeholder": "Last Name",
        },
        "email": {
            "placeholder": "Email",
        },
        "role": {
            "placeholder": "Role",
            "class": "form-control bg-danger text-white",
        },
    }
    action_disallowed_list = [
        "delete",
    ]
    can_view_details = True
    can_edit = True
    can_create = True
    details_modal = True
    edit_modal = True

    column_extra_row_actions = [
        # LinkRowAction("fa fa-user", "/admin/user/{row_id}/", "Visit Profile"),
        EndpointLinkRowAction("fa fa-user", "user.profile", "Visit Profile", id_arg="id"),
    ]

    @expose(url="/<int:id>", methods=["GET"])
    def profile(self, id):
        record: User = self.session.query(self.model).filter(self.model.id == id).first()
        if not record:
            flash(f"User with {id} id does not exist", "error")
            return redirect(url_for("user.index_view"))
        return self.render("admin/profile.html", username=record.username)
