from flask_wtf import FlaskForm
from wtforms import PasswordField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


class RegisterForm(FlaskForm):
    username = StringField("Kullanıcı Adı", validators=[DataRequired()])
    password = PasswordField("Parola", validators=[DataRequired()])
    password_again = PasswordField("Parola Tekrar", validators=[DataRequired(), EqualTo("password")])
    name = StringField("Ad", validators=[DataRequired()])
    surname = StringField("Soyad", validators=[DataRequired()])
    email = StringField("E-posta", validators=[DataRequired(), Email()])
    submit = SubmitField("Kayıt Ol")


class LoginForm(FlaskForm):
    username = StringField("Kullanıcı Adı", validators=[DataRequired()])
    password = PasswordField("Parola", validators=[DataRequired()])
    submit = SubmitField("Giriş Yap")


class ChangePasswordForm(FlaskForm):
    password = PasswordField("Parola", validators=[DataRequired()])
    new_password = PasswordField("Yeni Parola", validators=[DataRequired()])
    new_password_again = PasswordField("Yeni Parola Tekrar", validators=[DataRequired(), EqualTo("new_password")])
    submit = SubmitField("Şifreyi Değiştir")


class EditProfileForm(FlaskForm):
    name = StringField("Ad", validators=[DataRequired()])
    surname = StringField("Soyad", validators=[DataRequired()])
    email = StringField("E-posta", validators=[DataRequired(), Email()])
    submit = SubmitField("Değişiklikleri Kaydet")
