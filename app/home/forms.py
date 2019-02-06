from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError, IntegerField, SelectField, RadioField
from wtforms.validators import DataRequired

class Search(FlaskForm):
	lease_type = SelectField('Lease Type',choices=[('f','Family'),('a','Anyone'),('c','Company')], validators=[DataRequired()])
	furnished = RadioField('Furnished or Not',choices=[('0','Not Furnished'),('1','Furnished')] , validators=[DataRequired()])
	rooms = SelectField('Enter BHK',choices=[('1','1BHK'),('2','2BHK'),('3','3BHK'),('4','4BHK')], validators=[DataRequired()])
	submit = SubmitField('Search')