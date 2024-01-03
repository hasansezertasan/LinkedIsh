from flask_admin import Admin
from flask_admin.menu import MenuLink

from database.engine import LocalSession
from database.models import (
    Announcement,
    AnonymousFeedback,
    Audience,
    City,
    Company,
    CompanyDepartment,
    Country,
    EmailTemplate,
    Feedback,
    MemberFeedback,
    School,
    SchoolDepartment,
    Skill,
    User,
)

from .views import (
    AnnouncementModelView,
    AnonymousFeedbackView,
    AudienceModelView,
    CityModelView,
    CompanyDepartmentModelView,
    CompanyModelView,
    CountryModelView,
    EmailTemplateModelView,
    FeedbackModelView,
    IndexView,
    MemberFeedbackView,
    PingView,
    SchoolDepartmentModelView,
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
admin.add_category(name="Dynamic")
admin.add_category(name="Extra")
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
    SchoolDepartmentModelView(
        model=SchoolDepartment,
        session=LocalSession(),
        name="Departments",
        category="Educations",
        endpoint="school-department",
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
    CompanyDepartmentModelView(
        model=CompanyDepartment,
        session=LocalSession(),
        name="Company Departments",
        category="Experiences",
        endpoint="company-department",
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
    SkillModelView(
        model=Skill,
        session=LocalSession(),
        name="Skills",
        category="Store",
        endpoint="skill",
    )
)
admin.add_view(
    AudienceModelView(
        model=Audience,
        session=LocalSession(),
        name="Audiences",
        category="Store",
        endpoint="audience",
    )
)
admin.add_view(
    AnnouncementModelView(
        model=Announcement,
        session=LocalSession(),
        name="Announcements",
        category="Dynamic",
        endpoint="announcement",
    )
)
admin.add_view(
    FeedbackModelView(
        model=Feedback,
        session=LocalSession(),
        name="Feedbacks",
        category="Dynamic",
        endpoint="feedback",
    )
)
admin.add_view(
    MemberFeedbackView(
        model=MemberFeedback,
        session=LocalSession(),
        name="Member Feedbacks",
        category="Dynamic",
        endpoint="member-feedback",
    )
)
admin.add_view(
    AnonymousFeedbackView(
        model=AnonymousFeedback,
        session=LocalSession(),
        name="Anonymous Feedbacks",
        category="Dynamic",
        endpoint="anonymous-feedback",
    )
)
admin.add_view(
    EmailTemplateModelView(
        model=EmailTemplate,
        session=LocalSession(),
        name="Email Templates",
        category="Store",
        endpoint="email-template",
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
