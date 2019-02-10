from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, RadioField, ValidationError, IntegerField, SelectField
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
    user_type = RadioField('What Defines You', choices=[(
        'I', 'Investor'), ('L', 'Landlord')], validators=[DataRequired()])
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


class CompleteProfileForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    aadhar = StringField('Aadhar', validators=[DataRequired()])
    clear_survey = StringField('Survey', validators=[DataRequired()])
    mobile = StringField('Mobile No.', validators=[DataRequired()])
    land_pass_book = StringField('Land Pass Book', validators=[DataRequired()])
    state = SelectField('State', choices=[(
        'ap', 'Andhra Pradesh'), ('wb', 'West Bengal'), ('kr', 'Karnataka')], validators=[DataRequired()])
    district = SelectField('District', choices=[(
        'ap', 'Andhra Pradesh'), ('wb', 'West Bengal'), ('kr', 'Karnataka')], validators=[DataRequired()])
    mandal = StringField('mandal', validators=[DataRequired()])
    village = StringField('Village.', validators=[DataRequired()])
    zip_code = StringField('Zip Code', validators=[DataRequired()])
    land_address = StringField('Land Address', validators=[DataRequired()])
    residence_address = StringField(
        'Residence Address', validators=[DataRequired()])
    pan = StringField('PAN', validators=[DataRequired()])
    crop = StringField('Last Crop Details', validators=[DataRequired()])
    water = RadioField('Water Availability', choices=[(
        '1', 'Yes'), ('0', 'No')], validators=[DataRequired()])
    bank = StringField('bank', validators=[DataRequired()])

    submit = SubmitField('Complete')
