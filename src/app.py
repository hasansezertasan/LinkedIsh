from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_login import LoginManager

from database.base import Base
from database.engine import LocalSession, sync_engine
from database.models import User
from src import blueprints
from src.admin.blueprint import admin
from src.config import config
from src.driver import StorageManager  # noqa: F401

app = Flask(__name__)
app.config.update(config)
login_manager = LoginManager()
ckeditor = CKEditor(app)
bootstrap = Bootstrap5(app)

admin.init_app(app)
login_manager.init_app(app)
login_manager.login_view = "account.login"


@login_manager.user_loader
def load_user(user_id):
    with LocalSession() as db:
        return db.query(User).get(user_id)


@app.before_request
def before_request():
    print("Before Request.")


@app.after_request
def after_request(response):
    print("After Request.")
    return response


# Error Handlers
@app.errorhandler(400)
def bad_request(error):
    return render_template("error_pages/400.html"), 400


@app.errorhandler(401)
def unauthorized(error):
    return render_template("error_pages/401.html"), 401


@app.errorhandler(403)
def forbidden(error):
    return render_template("error_pages/403.html"), 403


@app.errorhandler(404)
def page_not_found(error):
    return render_template("error_pages/404.html"), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return render_template("error_pages/405.html"), 405


@app.errorhandler(500)
def internal_server_error(error):
    return render_template("error_pages/500.html"), 500


# Register Blueprints
app.register_blueprint(blueprints.home, url_prefix="/")
app.register_blueprint(blueprints.account, url_prefix="/account")

if __name__ == "__main__":
    with app.app_context():
        Base.metadata.create_all(sync_engine)
    app.run(debug=True, port=5000)
