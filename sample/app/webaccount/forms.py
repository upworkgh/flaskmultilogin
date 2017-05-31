from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, IntegerField, SelectField
from wtforms.validators import InputRequired, Email, Length

class LoginForm(Form):
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('Remember Me')

class RegisterForm(Form):
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    language = SelectField('Languages', choices=[('English', 'English'), ('Spanish', 'Spanish'), ('French', 'French')], validators=[InputRequired()])
    number = SelectField('Number of Web Accounts', choices=[('1', '1'), ('3', '3'), ('5', '5')], validators=[InputRequired()])

class WebAccountRegisterForm(Form):
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    language = SelectField('Languages', choices=[('English', 'English'), ('Spanish', 'Spanish'), ('French', 'French')], validators=[InputRequired()])
