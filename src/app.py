from flask import Flask
from flask_login import LoginManager

from database.base import Base
from database.engine import LocalSession, sync_engine
from database.models import User
from src import blueprints
from src.admin.config import admin
from src.config import config

app = Flask(__name__)
app.config.update(config)
login_manager = LoginManager()


admin.init_app(app)
login_manager.init_app(app)
login_manager.login_view = "account.login"


@login_manager.user_loader
def load_user(user_id):
    with LocalSession() as db:
        return db.query(User).get(user_id)


@app.before_request
def before_request():
    Base.metadata.create_all(sync_engine)


# Register Blueprints
app.register_blueprint(blueprints.home, url_prefix="/")
app.register_blueprint(blueprints.account, url_prefix="/account")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
