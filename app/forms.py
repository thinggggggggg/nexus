from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField(validators=[DataRequired()], id="form_item")
    password = PasswordField(validators=[DataRequired()], id="form_item")
    remember_me = BooleanField('Remember Me', id="boolean_form_item")
    submit = SubmitField('Sign In', id="form_item")