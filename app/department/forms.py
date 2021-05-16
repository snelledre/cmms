from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import Department


class BaseForm(FlaskForm):
    name = StringField('Naam', validators=[DataRequired(message=u'Dit veld is verplicht.'), Length(2, 64, message=u'Het veld moet tussen de 2 en 64 tekens lang zijn.')], render_kw={'class': 'form-control'})
    description = TextAreaField('Omschrijving', render_kw={'class': 'form-control', 'rows': 7})

    submit = SubmitField('Verstuur', render_kw={'class': 'btn btn-primary'})


class DepartmentForm(BaseForm):

    def validate_name(self, field):
        if Department.query.filter_by(name=field.data[0].upper() + field.data[1:].lower()).first():
            raise ValidationError('Afdeling is al geregistreerd. ')


class DepartmentEditForm(BaseForm):

    def __init__(self, original_name, *args, **kwargs):
        super(DepartmentEditForm, self).__init__(*args, **kwargs)
        self.original_name = original_name

    def validate_name(self, name):
        if name.data != self.original_name:
            department = Department.query.filter_by(name=self.name.data[0].upper() + name.data[1:].lower()).first()
            if department is not None:
                raise ValidationError('Afdeling is al geregistreerd.')
