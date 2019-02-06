from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError, IntegerField , SelectField, RadioField
from wtforms.validators import DataRequired

class PropertyRent(FlaskForm):

	name = StringField('Property Name', validators=[DataRequired()])
	lease_type = SelectField('Lease Type', choices=[('f','Family'),('a','Anyone'),('c','Company')], validators=[DataRequired()])
	furnished = RadioField(u'Furnished or Not',choices=[('0','Not Furnished'),('1','Furnished')] , validators=[DataRequired()])
	address = StringField('Address', validators=[DataRequired()])
	rooms = StringField('No of Rooms', validators=[DataRequired()])
	submit = SubmitField('Submit')