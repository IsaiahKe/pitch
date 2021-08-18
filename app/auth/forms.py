from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,ValidationError,BooleanField,TextAreaField
from wtforms.validators import Required,Email,EqualTo
from ..models import User



class UserRegistration(FlaskForm):
    username=StringField('Username',validators=[Required()])
    email=StringField('User Email',validators=[Required(),Email()])
    bio=TextAreaField(label="Biography",validators=[Required()])
    password=PasswordField("User password",validators=[Required(),EqualTo('password_confirm',message="Passwords Dont match!")])
    password_confirm=PasswordField(label="Confirm Password",validators=[Required()])
    submit=SubmitField('Register')
    
    def check_email(self,data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('There Email is already used')
        
    def check_username(self,data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError("The Username is already in use")
        
class UserLogin(FlaskForm):
    email=StringField('Enter user email', validators=[Required(),Email()])
    password=PasswordField('Enter password',validators=[Required()])
    remember=BooleanField('Remember me')
    submit=SubmitField('Continue')