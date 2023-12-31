from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

from database.engine import LocalSession
from database.models import User
from database.types import UserRole
from src.forms.user import ChangePasswordForm, EditProfileForm, LoginForm, RegisterForm

blueprint = Blueprint("account", __name__)


@blueprint.route("/login", endpoint="login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        if current_user.role == UserRole.SUPERUSER:
            return redirect(url_for("admin.index"))
        return redirect(url_for("home.index"))
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        with LocalSession() as db:
            user = db.query(User).filter_by(username=username).first()
            if user and user.verify_password(password):
                login_user(user)
                if user.role == UserRole.SUPERUSER:
                    return redirect(url_for("admin.index"))
                return redirect(url_for("home.index"))
            else:
                return render_template("account/login.html", form=form, error="Invalid username or password.")
    return render_template("account/login.html", form=form)


@blueprint.route(rule="/register", endpoint="register", methods=["GET", "POST"])
def register():
    # Eğer bir kullanıcı giriş yaptığı halde register endpointini ziyaret ederse, o kullanıcıyı gerekli sayfalara yönlendiriyoruz.
    if current_user.is_authenticated:
        if current_user.role == UserRole.SUPERUSER:
            return redirect(url_for("admin.index"))
        return redirect(url_for("home.index"))

    form = RegisterForm()
    if request.method == "POST" and form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        with LocalSession() as db:
            found = db.query(User).filter_by(username=username).first()
            if found:
                return render_template("account/register.html", form=form, error="Username already exists.")

            user = User(
                username=username,
                password=password,
                name=name,
                surname=surname,
                email=email,
            )
            db.add(user)
            db.commit()
            return render_template(
                "account/register.html",
                form=form,
                error="Thank you for registering. Please login.",
            )
    return render_template("account/register.html", form=form)


@blueprint.get(rule="/logout", endpoint="logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("account.login"))


@blueprint.route(rule="/edit", endpoint="edit", methods=["GET", "POST"])
@login_required
def edit():
    form = EditProfileForm(obj=current_user._get_current_object())
    if request.method == "POST" and form.validate_on_submit():
        with LocalSession() as db:
            user = db.query(User).filter_by(username=current_user.username).first()
            if user:
                current_user.name = form.name.data
                current_user.surname = form.surname.data
                current_user.email = form.email.data
                db.commit()
                return render_template("account/edit.html", form=form, error="Profile updated.")
            return render_template("account/edit.html", form=form, error="User not found.")
    return render_template("account/edit.html", form=form)


@blueprint.route(
    rule="/password/change",
    endpoint="password_change",
    methods=["GET", "POST"],
)
@login_required
def password_change():
    form = ChangePasswordForm()
    if request.method == "POST" and form.validate_on_submit():
        if form.new_password.data != form.new_password_again.data:
            return render_template(
                "account/password-change.html",
                form=form,
                error="New passwords do not match.",
            )
        with LocalSession() as db:
            user = db.query(User).filter_by(username=current_user.username).first()
            if user and user.verify_password(form.password.data):
                current_user.password = form.new_password.data
                db.commit()
                return redirect(url_for("account.logout"))
            return render_template("account/password-change.html", form=form, error="Invalid password.")
    return render_template("account/password-change.html", form=form)


# blueprint.add_url_rule(rule='/password/reset', endpoint='password_reset', view_func=password_reset, methods=['GET', 'POST'])
