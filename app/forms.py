from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):  # might change... css is better. looks nicer
    username = StringField(validators=[DataRequired()], id="input_field")
    password = PasswordField(validators=[DataRequired()], id="input_field")
    remember_me = BooleanField('Remember Me', id="boolean_field")
    submit = SubmitField('Sign In', id="submit_field")