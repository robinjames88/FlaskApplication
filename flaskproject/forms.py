from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,EqualTo,Email
from wtforms import ValidationError
from flaskproject.models import User

# Create registration form using flask form
class RegistrationForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired(), EqualTo('confirm_pass',message='Password not matching')])
    confirm_pass = PasswordField('Confirm Password',validators=[DataRequired()])
    submit = SubmitField('Register')


    # Method querys the table for email id and raises error for duplicate email id 
    def validate_email(self, email):
        if User.query.filter_by(email=self.email.data).first():
            raise ValidationError('Email already used.!')

# Create Login form using flask form
class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Login')


