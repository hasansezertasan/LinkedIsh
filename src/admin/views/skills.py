from database.models import Skill
from src.admin.views.mixins import BaseModelView


class SkillModelView(BaseModelView):
    column_list = [
        Skill.id,
        Skill.date_created,
        Skill.date_updated,
        Skill.name,
    ]
    column_labels = {
        Skill.id: "ID",
        Skill.date_created: "Date Created",
        Skill.date_updated: "Date Updated",
        Skill.name: "Name",
    }
    column_searchable_list = [
        Skill.name,
    ]
    column_sortable_list = [
        Skill.id,
        Skill.date_created,
        Skill.date_updated,
        Skill.name,
    ]
    column_filters = [
        Skill.id,
        Skill.date_created,
        Skill.date_updated,
        Skill.name,
    ]
    form_columns = [
        Skill.name,
    ]
    can_view_details = True
    details_modal = True
    can_edit = True
    can_create = True
    can_delete = True
    page_size = 50
