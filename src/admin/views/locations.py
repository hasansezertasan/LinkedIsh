from flask import flash
from flask_admin.actions import action
from markupsafe import Markup

from database.models import City, Country
from src.admin.views.mixins import BaseModelView


class CountryModelView(BaseModelView):
    column_list = [
        Country.id,
        Country.date_created,
        Country.date_updated,
        Country.name,
        "city_count",
        "cities",
    ]
    column_details_list = [
        Country.id,
        Country.date_created,
        Country.date_updated,
        Country.name,
        "city_count",
        "cities",
    ]
    column_labels = {
        Country.id: "ID",
        Country.date_created: "Date Created",
        Country.date_updated: "Date Updated",
        Country.name: "Name",
        "city_count": "City Count",
        "cities.id": "City ID",
        "cities": "Cities",
    }
    column_descriptions = {
        "city_count": "City Count",
        "cities.id": "City ID",
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
        "cities.id",
        "cities",
    ]
    column_formatters = {
        "city_count": lambda v, c, m, p: len(m.cities),
        "cities": lambda v, c, m, p: Markup(
            "<br>".join([f'<a href="/admin/city/{city.id}/view">{city.name}</a>' for city in m.cities[:3]])
        ),
    }
    form_columns = [
        Country.name,
    ]
    inline_models = [
        (
            City,
            dict(
                form_columns=[
                    City.id,
                    City.name,
                ],
            ),
        ),
    ]
    can_view_details = True
    can_edit = True
    can_create = True
    can_delete = True
    details_modal = True
    edit_modal = True
    create_modal = True
    page_size = 50

    @action(
        name="count",
        text="Count Cities",
        confirmation="Are you sure you want to count the cities?",
    )
    def action_recalculate(self, ids):
        count = 0
        for proxy in self.get_query().filter(
            self.model.id.in_(ids),
        ):
            count += len(proxy.cities)
        flash(f"Counted {count} cities", "success")


class CityModelView(BaseModelView):
    column_labels = {
        City.id: "ID",
        City.date_created: "Date Created",
        City.date_updated: "Date Updated",
        City.name: "Name",
        "country.name": "Country",
    }
    column_searchable_list = [
        City.name,
    ]
    column_sortable_list = [
        City.id,
        City.date_created,
        City.date_updated,
        City.name,
        "country.name",
    ]
    column_filters = [
        City.id,
        City.date_created,
        City.date_updated,
        City.name,
        "country.id",
        "country",
    ]
    form_columns = [
        City.name,
        "country",
    ]
    can_view_details = True
    details_modal = True
    can_edit = True
    can_create = True
    can_delete = True
    page_size = 50
