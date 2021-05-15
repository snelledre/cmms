from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp
from wtforms import ValidationError
from ..models import Role, User


class NameForm(FlaskForm):
    name = StringField('Wat is je volledige naam?', validators=[DataRequired()])
    submit = SubmitField('Verstuur')


class EditProfileForm(FlaskForm):
    name = StringField('Real name', validators=[Length(0, 64)])
    submit = SubmitField('Verstuur')


class EditProfileAdminForm(FlaskForm):
    email = StringField('E-mailadres', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    username = StringField('Gebruikersnaam', validators=[
        DataRequired(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               'Gebruikersnamen mogen alleen letters, cijfers, punten of onderstrepingstekens bevatten')])
    confirmed = BooleanField('Confirmed')
    role = SelectField('Rol', coerce=int)
    name = StringField('Volledige naam', validators=[Length(0, 64)])
    submit = SubmitField('Verstuur')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)
                             for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and \
                User.query.filter_by(email=field.data).first():
            raise ValidationError('E-mailadres al geregistreerd.')

    def validate_username(self, field):
        if field.data != self.user.username and \
                User.query.filter_by(username=field.data).first():
            raise ValidationError('Gebruikersnaam is al in gebruik.')
