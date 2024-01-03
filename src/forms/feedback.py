from flask_wtf import FlaskForm
from wtforms import EmailField, SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

from database.types import FeedbackCategory


class FeedbackForm(FlaskForm):
    subject = StringField(
        label="Konu",
        validators=[DataRequired()],
    )
    content = TextAreaField(
        label="İçerik",
        validators=[DataRequired()],
    )
    category = SelectField(
        label="Kategori",
        choices=[(category.value, category.value) for category in FeedbackCategory],
        validators=[DataRequired()],
    )


class MemberFeedbackForm(FeedbackForm):
    submit = SubmitField(
        label="Gönder",
        description="Geri bildiriminizi göndermek için tıklayın.",
        render_kw={
            "class": "btn btn-lg btn-dark btn-block form-control",
        },
    )


class AnonymousFeedbackForm(FeedbackForm):
    email = EmailField(
        label="E-posta",
        validators=[DataRequired(), Email()],
    )
    submit = SubmitField(
        label="Gönder",
        description="Geri bildiriminizi göndermek için tıklayın.",
        render_kw={
            "class": "btn btn-lg btn-dark btn-block form-control",
        },
    )
