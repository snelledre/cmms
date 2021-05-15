from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(2, 64),
                                             Email()])
    password = PasswordField('Wachtwoord', validators=[DataRequired()])
    remember_me = BooleanField('Herinner mij')
    submit = SubmitField('Inloggen')


class RegistrationForm(FlaskForm):
    email = StringField('E-mailadres', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    username = StringField('Gebruikersnaam', validators=[
        DataRequired(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               'Gebruikersnamen mogen alleen letters, cijfers, punten of onderstrepingstekens bevatten ')])
    password = PasswordField('Wachtwoord', validators=[
        DataRequired(), EqualTo('password2', message='Wachtwoorden moeten overeenkomen.')])
    password2 = PasswordField('Herhaal wachtwoord', validators=[DataRequired()])
    submit = SubmitField('Registeren')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('E-mailadres is al geregistreerd. ')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Gebruikersnaam is al in gebruik.')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Huidig wachtwoord', validators=[DataRequired()])
    password = PasswordField('Nieuw wachtwoord', validators=[
        DataRequired(), EqualTo('password2', message='Wachtwoorden moeten overeenkomen.')])
    password2 = PasswordField('Herhaal nieuw wachtwoord',
                              validators=[DataRequired()])
    submit = SubmitField('Verzenden')


class PasswordResetRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    submit = SubmitField('Wachtwoord opniew instellen')


class PasswordResetForm(FlaskForm):
    password = PasswordField('Nieuw wachtwoord', validators=[
        DataRequired(), EqualTo('password2', message='Wachtwoorden moeten overeenkomen.')])
    password2 = PasswordField('Herhaal wachtwoord', validators=[DataRequired()])
    submit = SubmitField('Verzenden')


class ChangeEmailForm(FlaskForm):
    email = StringField('Nieuw e-mailadres', validators=[DataRequired(), Length(1, 64),
                                                 Email()])
    password = PasswordField('Wachtwoord', validators=[DataRequired()])
    submit = SubmitField('E-mailadres opnieuw instellen')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('E-mailadres al geregistreerd. ')
