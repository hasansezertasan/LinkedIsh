from flask import Flask
from flask_login import LoginManager

from database.engine import LocalSession
from database.models import User
from src import blueprints
from src.admin.config import admin
from src.config import config

app = Flask(__name__)
app.config.update(config)
login_manager = LoginManager()


admin.init_app(app)
login_manager.init_app(app)
login_manager.login_view = "user.login"


@login_manager.user_loader
def load_user(user_id):
    with LocalSession() as db:
        return db.query(User).get(user_id)


# Register Blueprints
app.register_blueprint(blueprints.home, url_prefix="/")
app.register_blueprint(blueprints.user, url_prefix="/user")
