from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField(validators=[DataRequired()], id="username-entry")
    password = PasswordField(validators=[DataRequired()], id="password-entry")
    remember_me = BooleanField('Remember Me', id="boolean-form-item")
    next = SubmitField('Next', id="next-entry")
    submit = SubmitField('Sign In', id="submit-entry")