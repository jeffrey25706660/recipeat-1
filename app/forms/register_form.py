from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired()])
    username = StringField('Username (Email Address)', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    age = IntegerField('Age (Number)')
    height = IntegerField('Height (Number)')
    weight = IntegerField('Weight (Number)')
    gender = RadioField('Gender', choices=['Male', 'Female'], default='Male')
    submit = SubmitField('Register')
