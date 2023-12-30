from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


class RegisterForm(FlaskForm):
    username = StringField(
        label="Kullanıcı Adı",
        validators=[DataRequired()],
    )
    password = PasswordField(
        label="Parola",
        validators=[DataRequired()],
    )
    password_again = PasswordField(
        label="Parola Tekrar",
        validators=[DataRequired(), EqualTo("password")],
    )
    name = StringField(
        label="Ad",
        validators=[DataRequired()],
    )
    surname = StringField(
        label="Soyad",
        validators=[DataRequired()],
    )
    email = StringField(
        label="E-posta",
        validators=[DataRequired(), Email()],
    )
    submit = SubmitField(
        label="Kayıt Ol",
        description="Kayıt olmak için tıklayın.",
    )


class LoginForm(FlaskForm):
    username = StringField(
        label="Kullanıcı Adı",
        validators=[DataRequired()],
        description="Kullanıcı adınızı girin.",
    )
    password = PasswordField(
        label="Parola",
        validators=[DataRequired()],
    )
    submit = SubmitField(
        label="Giriş Yap",
        description="Giriş yapmak için tıklayın.",
    )


class ChangePasswordForm(FlaskForm):
    password = PasswordField(
        label="Parola",
        validators=[DataRequired()],
    )
    new_password = PasswordField(
        label="Yeni Parola",
        validators=[DataRequired()],
    )
    new_password_again = PasswordField(
        label="Yeni Parola Tekrar",
        validators=[DataRequired(), EqualTo("new_password")],
    )
    submit = SubmitField(
        label="Şifreyi Değiştir",
        description="Şifrenizi değiştirmek için tıklayın.",
    )


class EditProfileForm(FlaskForm):
    name = StringField(
        label="Ad",
        validators=[DataRequired()],
    )
    surname = StringField(
        label="Soyad",
        validators=[DataRequired()],
    )
    email = StringField(
        label="E-posta",
        validators=[DataRequired(), Email()],
    )
    submit = SubmitField(
        label="Değişiklikleri Kaydet",
        description="Profil bilgilerini güncellemek için tıklayın.",
    )
