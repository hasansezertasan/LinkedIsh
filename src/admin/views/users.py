from src.admin.views.mixins import BaseModelView


class UserModelView(BaseModelView):
    column_filters = [
        "id",
        "date_created",
        "username",
        "name",
        "surname",
        "email",
        "role",
    ]
    column_list = [
        "id",
        "username",
        "name",
        "surname",
        "role",
    ]
    column_labels = {
        "id": "ID",
        "date_created": "Created",
        "username": "Username",
        "password": "Password",
        "name": "Name of User",
        "surname": "Surname of User",
        "role": "Role",
    }
    column_descriptions = {
        "id": "User ID",
        "date_created": "The date the user was created",
        "username": "The username of the user",
        "name": "Name of the user",
        "surname": "Surname of the user",
        "password": "The password of the user",
        "role": "The role of the user",
    }
    column_choices = {
        "role": [
            ("admin", "Super User"),
            ("user", "Basic User"),
        ]
    }
    column_details_list = [
        "id",
        "date_created",
        "date_updated",
        "username",
        "name",
        "surname",
        "role",
    ]
    can_view_details = True
    details_modal = True
    can_edit = False
    can_create = False
