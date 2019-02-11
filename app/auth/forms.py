from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, RadioField, ValidationError, IntegerField, SelectField, TextAreaField
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
    land_address = TextAreaField('Land Address', validators=[DataRequired()])
    residence_address = TextAreaField(
        'Residence Address', validators=[DataRequired()])
    pan = StringField('PAN', validators=[DataRequired()])
    crop = StringField('Last Crop Details', validators=[DataRequired()])
    water = RadioField('Water Availability', choices=[(
        '1', 'Yes'), ('0', 'No')], validators=[DataRequired()])
    account_no = StringField('account_no', validators=[DataRequired()])
    bank_name = StringField('bank_name', validators=[DataRequired()])
    ifsc = StringField('ifsc', validators=[DataRequired()])
    investment_amount = StringField(
        'investment_amount', validators=[DataRequired()])
    employment_type = RadioField('Are you a', choices=[(
        'salaried', 'Salaried Employee'), ('businessman', 'Businessman')], validators=[DataRequired()])

    submit = SubmitField('Complete')
