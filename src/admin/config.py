from flask_admin import Admin
from flask_admin.menu import MenuLink

from database.engine import LocalSession
from database.models import (
    Announcement,
    Audience,
    City,
    Company,
    Country,
    Department,
    Feedback,
    Language,
    Position,
    School,
    Skill,
    User,
)

from .views import (
    AnnouncementModelView,
    AudienceModelView,
    CityModelView,
    CompanyModelView,
    CountryModelView,
    DepartmentModelView,
    FeedbackModelView,
    IndexView,
    LanguageModelView,
    PingView,
    PositionModelView,
    SchoolModelView,
    SkillModelView,
    UserModelView,
)

admin = Admin(
    name="LinkedIsh Admin Panel",
    index_view=IndexView(),
    template_mode="bootstrap4",
)

# Categories
admin.add_category(name="Store")
admin.add_category(name="Extra")
admin.add_category(name="Dynamic")
admin.add_sub_category(name="Feedbacks", parent_name="Dynamic")
admin.add_sub_category(name="Audiences", parent_name="Store")
admin.add_sub_category(name="Skills", parent_name="Store")
admin.add_sub_category(name="Announcements", parent_name="Dynamic")
admin.add_sub_category(name="Languages", parent_name="Store")
admin.add_sub_category(name="Locations", parent_name="Store")
admin.add_sub_category(name="Experiences", parent_name="Store")
admin.add_sub_category(name="Educations", parent_name="Store")

# Menu Links
admin.add_link(
    MenuLink(
        name="LinkedIsh",
        url="/",
        category="Extra",
    )
)
# Custom Views
admin.add_view(
    PingView(
        name="Ping",
        category="Extra",
    )
)

# Model Views
admin.add_view(
    SchoolModelView(
        model=School,
        session=LocalSession(),
        name="Schools",
        category="Educations",
        endpoint="school",
    )
)
admin.add_view(
    DepartmentModelView(
        model=Department,
        session=LocalSession(),
        name="Departments",
        category="Educations",
        endpoint="department",
    )
)
admin.add_view(
    CompanyModelView(
        model=Company,
        session=LocalSession(),
        name="Companies",
        category="Experiences",
        endpoint="company",
    )
)
admin.add_view(
    PositionModelView(
        model=Position,
        session=LocalSession(),
        name="Positions",
        category="Experiences",
        endpoint="position",
    )
)
admin.add_view(
    CountryModelView(
        model=Country,
        session=LocalSession(),
        name="Countries",
        category="Locations",
        endpoint="country",
    )
)
admin.add_view(
    CityModelView(
        model=City,
        session=LocalSession(),
        name="Cities",
        category="Locations",
        endpoint="city",
    )
)
admin.add_view(
    LanguageModelView(
        model=Language,
        session=LocalSession(),
        name="Languages",
        category="Languages",
        endpoint="language",
    )
)
admin.add_view(
    SkillModelView(
        model=Skill,
        session=LocalSession(),
        name="Skills",
        category="Skills",
        endpoint="skill",
    )
)
admin.add_view(
    AudienceModelView(
        model=Audience,
        session=LocalSession(),
        name="Audiences",
        category="Audiences",
        endpoint="audience",
    )
)
admin.add_view(
    AnnouncementModelView(
        model=Announcement,
        session=LocalSession(),
        name="Announcements",
        category="Announcements",
        endpoint="announcement",
    )
)
admin.add_view(
    FeedbackModelView(
        model=Feedback,
        session=LocalSession(),
        name="Feedbacks",
        category="Feedbacks",
        endpoint="feedback",
    )
)
admin.add_view(
    UserModelView(
        model=User,
        session=LocalSession(),
        name="Users",
        endpoint="user",
    )
)
