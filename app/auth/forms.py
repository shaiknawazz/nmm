from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, RadioField, ValidationError, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo
from ..models import Users

class LoginForm(FlaskForm):

	#username = StringField('Username', validators=[DataRequired()])
    mobile_no = StringField('Mobile No.', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    mobile_no = StringField('Mobile No.', validators=[DataRequired()])
    #username = StringField('Username', validators=[DataRequired()])
    user_type = RadioField('What You Want to Do',choices=[('L','Give on Rent'),('T','Take on Rent')] , validators=[DataRequired()])
    password = PasswordField('Password', validators=[
                                        DataRequired(),
                                        EqualTo('confirm_password')
                                        ])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Register')

    def validate_email(self, field):
        if Users.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')

    '''def validate_username(self, field):
        if Users.query.filter_by(username=field.data).first():
            raise ValidationError('Username is already in use.')'''

    def validate_mobile_no(self, field):
        if Users.query.filter_by(mobile_no=field.data).first():
            raise ValidationError('Mobile No. is already in use.')