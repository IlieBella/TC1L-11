from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class UpdateProfileForm(FlaskForm):
    username = StringField('Username', 
                           validators=[DataRequired(), Length(min=3, max=20)])
    name = StringField('Name',
                        validators=[DataRequired(), Length(min=3, max=50)])
    email = StringField('Email', 
                        validators=[DataRequired(), Email()])
    phonenumber = StringField('Phone number',
                               validators=[DataRequired(), Length(min=10, max=12)])
    submit = SubmitField('Update Profile')
 