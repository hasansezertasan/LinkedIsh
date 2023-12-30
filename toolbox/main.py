import os

import typer

from database.engine import Base, LocalSession, sync_engine
from database.models import (
    Announcement,
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

app = typer.Typer()
basedir = os.path.abspath(os.path.dirname(__file__))


@app.command(help="Create database", short_help="Create database")
def create_db():
    """
    Create database

    Usage:
        python toolbox create-db
    """
    Base.metadata.create_all(sync_engine)


@app.command(help="Create Admin", short_help="Create Admin")
def create_admin():
    """
    Usage:
        python toolbox create-admin
    """
    Base.metadata.create_all(bind=sync_engine)
    with LocalSession() as db:
        db.commit()
        admin_credentials = {
            "username": "superuser",
            "password": "superuser",
            "name": "superuser",
            "surname": "superuser",
            "email": "superuser@superuser.com",
        }
        user = db.query(User).filter_by(username=admin_credentials["username"]).first()
        if not user:
            user = User(**admin_credentials)
            user.role = "admin"
            db.add(user)
        db.commit()


@app.command(help="Add Countries and Cities", short_help="Add Countries and Cities")
def add_countries_and_cities():
    pass


@app.command(help="Add Skills", short_help="Add Skills")
def add_skills():
    pass


@app.command(help="Add Languages", short_help="Add Languages")
def add_languages():
    pass


@app.command(help="Add Schools", short_help="Add Schools")
def add_schools():
    pass


@app.command(help="Add Departments", short_help="Add Departments")
def add_departments():
    pass


@app.command(help="Add Companies", short_help="Add Companies")
def add_companies():
    pass


@app.command(help="Add Positions", short_help="Add Positions")
def add_positions():
    pass


@app.command(help="Add Audiences", short_help="Add Audiences")
def add_audiences():
    pass


if __name__ == "__main__":
    app()
