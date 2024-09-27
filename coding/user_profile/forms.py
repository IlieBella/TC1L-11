from flask import FlaskForm
from forms import StringField, SubmitField
from forms import DataRequired, Length, Email

class UpdateProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Update')
