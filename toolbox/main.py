import datetime
import json
import os

import typer

from database.base import Base
from database.engine import LocalSession, sync_engine
from database.models import (
    Announcement,
    AnonymousFeedback,
    City,
    Company,
    CompanyDepartment,
    Country,
    Feedback,
    MemberFeedback,
    School,
    SchoolDepartment,
    Skill,
    User,
)
from database.types import UserRole
from src.config import basedir

app = typer.Typer()


@app.command(help="Create database")
def create_database():
    """
    Create database

    Usage:
        python toolbox create-database
    """
    Base.metadata.create_all(bind=sync_engine)


@app.command(help="Seed Users Table")
def seed_users_table():
    """
    Seed Users Table

    Usage:
        python toolbox seed-users-table
    """
    path = os.path.join(basedir, "tests", "assets", "users.json")
    with open(path, "r", encoding="utf-8") as f:
        users = json.load(f)
    for idx, user in enumerate(users):
        users[idx]["hashed_password"] = user["password"]
        del users[idx]["password"]
        users[idx]["birth_date"] = datetime.datetime.strptime(user["birth_date"], "%Y-%m-%d")
    with LocalSession() as db:
        for user in users:
            db.add(User(**user))
        db.commit()


@app.command(help="Seed Skills Table")
def seed_skills_table():
    """
    Seed Skills Table

    Usage:
        python toolbox seed-skills-table
    """
    path = os.path.join(basedir, "tests", "assets", "skills.json")
    with open(path, "r", encoding="utf-8") as f:
        skills = json.load(f)
    with LocalSession() as db:
        for skill in skills:
            db.add(Skill(**skill))
        db.commit()


@app.command(help="Seed Feedbacks Table")
def seed_feedbacks_table():
    """
    Seed Feedbacks Table

    Usage:
        python toolbox seed-feedbacks-table
    """
    path = os.path.join(basedir, "tests", "assets", "feedbacks_anonymous.json")
    with open(path, "r", encoding="utf-8") as f:
        feedbacks = json.load(f)
    with LocalSession() as db:
        for feedback in feedbacks:
            db.add(AnonymousFeedback(**feedback))
        db.commit()
    path = os.path.join(basedir, "tests", "assets", "feedbacks_member.json")
    with open(path, "r", encoding="utf-8") as f:
        feedbacks = json.load(f)
    with LocalSession() as db:
        for feedback in feedbacks:
            user = db.query(User).filter_by(username=feedback["username"]).first()
            feedback["user_id"] = user.id
            del feedback["username"]
            db.add(MemberFeedback(**feedback))
        db.commit()


@app.command(help="Seed Locations Table")
def seed_locations_table():
    """
    Seed Locations Table

    Usage:
        python toolbox seed-locations-table
    """
    path = os.path.join(basedir, "tests", "assets", "locations.json")
    with open(path, "r", encoding="utf-8") as f:
        locations = json.load(f)
    with LocalSession() as db:
        for location in locations:
            country = Country(name=location["country"])
            cities = []
            for city in location["cities"]:
                cities.append(City(name=city))
            country.cities = cities
            db.add(country)
        db.commit()


@app.command(help="Seed Announcements Table")
def seed_announcements_table():
    """
    Seed Announcements Table

    Usage:
        python toolbox seed-announcements-table
    """
    path = os.path.join(basedir, "tests", "assets", "announcements.json")
    with open(path, "r", encoding="utf-8") as f:
        announcements = json.load(f)
    with LocalSession() as db:
        for announcement in announcements:
            user = db.query(User).filter_by(username=announcement["username"]).first()
            announcement["user_id"] = user.id
            del announcement["username"]
            db.add(Announcement(**announcement))
        db.commit()


@app.command(help="Create Admin")
def create_admin():
    """
    Usage:
        python toolbox create-admin
    """
    with LocalSession() as db:
        admin_credentials = {
            "username": "superuser",
            "hashed_password": "superuser",
            "first_name": "superuser",
            "last_name": "superuser",
            "email": "superuser@superuser.com",
            "role": UserRole.SUPERUSER,
        }
        user = db.query(User).filter_by(username=admin_credentials["username"]).first()
        if not user:
            user = User(**admin_credentials)
            db.add(user)
        db.commit()


@app.command(help="Add Countries and Cities")
def add_countries_and_cities():
    pass


@app.command(help="Add Skills")
def add_skills():
    pass


@app.command(help="Add Schools")
def add_schools():
    pass


@app.command(help="Add Departments")
def add_departments():
    pass


@app.command(help="Add Companies")
def add_companies():
    pass


@app.command(help="Add Positions")
def add_positions():
    pass


@app.command(help="Add Audiences")
def add_audiences():
    pass


if __name__ == "__main__":
    app()
