from src.admin.views.mixins import BaseModelView


class UserModelView(BaseModelView):
    column_filters = [
        "id",
        "date_created",
        "username",
        "first_name",
        "last_name",
        "email",
        "role",
    ]
    column_list = [
        "id",
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
        "username": "The username of the user",
        "first_name": "First Name",
        "last_name": "Last Name",
        "hashed_password": "The password of the user",
        "role": "The role of the user",
    }
    column_choices = {
        "role": [
            ("SUPERUSER", "Superuser"),
            ("ADMIN", "Admin"),
            ("USER", "User"),
            ("BLOCKED", "Blocked"),
        ]
    }
    column_details_list = [
        "id",
        "date_created",
        "date_updated",
        "username",
        "first_name",
        "last_name",
        "role",
    ]
    form_excluded_columns = [
        "date_created",
        "date_updated",
        "hashed_password",
    ]
    can_view_details = True
    details_modal = True
    can_edit = True
    can_create = True
