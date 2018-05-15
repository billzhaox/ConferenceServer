from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateTimeField
from wtforms.validators import DataRequired


class AddConferenceForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    date = DateTimeField('date', validators=[DataRequired()])
    place = StringField('place', validators=[DataRequired()])
    submit = SubmitField('submit')