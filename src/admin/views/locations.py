from database.models import City, Country
from src.admin.views.mixins import BaseModelView


class CountryModelView(BaseModelView):
    column_list = [
        Country.id,
        Country.date_created,
        Country.date_updated,
        Country.name,
        "cities",
    ]
    column_labels = {
        Country.id: "ID",
        Country.date_created: "Date Created",
        Country.date_updated: "Date Updated",
        Country.name: "Name",
        "cities": "Cities",
    }
    column_searchable_list = [
        Country.name,
    ]
    column_sortable_list = [
        Country.id,
        Country.date_created,
        Country.date_updated,
        Country.name,
    ]
    column_filters = [
        Country.id,
        Country.date_created,
        Country.date_updated,
        Country.name,
    ]
    column_details_list = [
        Country.id,
        Country.date_created,
        Country.date_updated,
        Country.name,
        "cities",
    ]
    form_columns = [
        Country.name,
    ]
    inline_models = [
        (
            City,
            dict(
                form_columns=["id", "name"],
            ),
        ),
    ]
    can_view_details = True
    details_modal = True
    can_edit = True
    can_create = True
    can_delete = True
    page_size = 50


class CityModelView(BaseModelView):
    column_labels = {
        City.id: "ID",
        City.date_created: "Date Created",
        City.date_updated: "Date Updated",
        City.name: "Name",
    }
    column_searchable_list = [
        City.name,
    ]
    column_sortable_list = [
        City.id,
        City.date_created,
        City.date_updated,
        City.name,
    ]
    column_filters = [
        City.id,
        City.date_created,
        City.date_updated,
        City.name,
    ]
    form_columns = [City.name, "country"]
    can_view_details = True
    details_modal = True
    can_edit = True
    can_create = True
    can_delete = True
    page_size = 50
