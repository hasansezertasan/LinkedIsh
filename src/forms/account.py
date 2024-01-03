from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


class RegisterForm(FlaskForm):
    username = StringField(
        label="Kullanıcı Adı",
        validators=[DataRequired()],
        render_kw={"size": 32, "class": "form-control", "placeholder": "Kullanıcı adınızı girin."},
    )
    password = PasswordField(
        label="Parola",
        validators=[DataRequired()],
        render_kw={"size": 32, "class": "form-control", "placeholder": "Parola girin."},
    )
    password_again = PasswordField(
        label="Parola Tekrar",
        validators=[DataRequired(), EqualTo("password")],
        render_kw={"size": 32, "class": "form-control", "placeholder": "Parolanızı Tekrar Girin."},
    )
    first_name = StringField(
        label="Ad",
        validators=[DataRequired()],
        render_kw={"size": 32, "class": "form-control", "placeholder": "Adınızı giriniz."},
    )
    last_name = StringField(
        label="Soyad",
        validators=[DataRequired()],
        render_kw={"size": 32, "class": "form-control", "placeholder": "Soy adınızı giriniz."},
    )
    email = EmailField(
        label="E-posta",
        validators=[DataRequired(), Email()],
        render_kw={"size": 32, "class": "form-control", "placeholder": "Email Adresinizi Girin."},
    )
    submit = SubmitField(
        label="Kayıt Ol",
        description="Kayıt olmak için tıklayın.",
        render_kw={
            "class": "btn btn-lg btn-dark btn-block form-control",
        },
    )


class LoginForm(FlaskForm):
    username = StringField(
        label="Kullanıcı Adı",
        validators=[DataRequired()],
        description="Kullanıcı adınızı girin.",
        render_kw={"size": 32, "class": "form-control", "placeholder": "Kullanıcı adınızı girin."},
    )
    password = PasswordField(
        label="Parola",
        validators=[DataRequired()],
        render_kw={"size": 32, "class": "form-control", "placeholder": "Parola girin."},
    )
    submit = SubmitField(
        label="Giriş Yap",
        description="Giriş yapmak için tıklayın.",
        render_kw={
            "class": "btn btn-lg btn-dark btn-block form-control",
        },
    )


class ChangePasswordForm(FlaskForm):
    password = PasswordField(
        label="Parola",
        validators=[DataRequired()],
        render_kw={"size": 32, "class": "form-control", "placeholder": "Parola girin."},
    )
    new_password = PasswordField(
        label="Yeni Parola",
        validators=[DataRequired()],
        render_kw={"size": 32, "class": "form-control", "placeholder": "Yeni parolanızı girin."},
    )
    new_password_again = PasswordField(
        label="Yeni Parola Tekrar",
        validators=[DataRequired(), EqualTo("new_password")],
        render_kw={"size": 32, "class": "form-control", "placeholder": "Yeni parolanızı tekrar girin."},
    )
    submit = SubmitField(
        label="Şifreyi Değiştir",
        description="Şifrenizi değiştirmek için tıklayın.",
        render_kw={
            "class": "btn btn-lg btn-dark btn-block form-control",
        },
    )


class EditProfileForm(FlaskForm):
    first_name = StringField(
        label="Ad",
        validators=[DataRequired()],
        render_kw={"size": 32, "class": "form-control", "placeholder": "Adınızı girin."},
    )
    last_name = StringField(
        label="Soyad",
        validators=[DataRequired()],
        render_kw={"size": 32, "class": "form-control", "placeholder": "Soy adınızı giriniz."},
    )
    email = StringField(
        label="E-posta",
        validators=[DataRequired(), Email()],
        render_kw={"size": 32, "class": "form-control", "placeholder": "Email Adresinizi Girin."},
    )
    submit = SubmitField(
        label="Değişiklikleri Kaydet",
        description="Profil bilgilerini güncellemek için tıklayın.",
        render_kw={
            "class": "btn btn-lg btn-dark btn-block form-control",
        },
    )
