from flask import Blueprint, jsonify, redirect, render_template, request, url_for
from flask_login import current_user

from database.engine import LocalSession
from database.models import AnonymousFeedback, MemberFeedback, User
from database.types import UserRole
from src.forms.feedback import AnonymousFeedbackForm, MemberFeedbackForm

blueprint = Blueprint("home", __name__)


@blueprint.get(
    rule="/",
    endpoint="index",
)
def index():
    return render_template("home/index.html")


@blueprint.route(
    rule="/ping",
    endpoint="ping",
    methods=["GET", "POST"],
)
def ping():
    value = {
        "message": "Pong!",
    }
    return jsonify(value)


@blueprint.route("/feedback", endpoint="feedback", methods=["GET", "POST"])
def login():
    form = None
    if current_user.is_authenticated:
        form = MemberFeedbackForm()
    else:
        form = AnonymousFeedbackForm()
    if request.method == "POST" and form.validate_on_submit():
        # Print every data from the form
        data = form.data
        data.pop("csrf_token")
        data.pop("submit")
        with LocalSession() as db:
            if isinstance(form, MemberFeedbackForm):
                feedback = MemberFeedback(**data)
                feedback.user_id = current_user.id
            else:
                feedback = AnonymousFeedback(**data)
            db.add(feedback)
            db.commit()
        return render_template(
            "home/index.html",
            form=form,
            success="Geri bildiriminiz başarıyla gönderildi.",
        )
    return render_template(
        "home/feedback.html",
        form=form,
    )
