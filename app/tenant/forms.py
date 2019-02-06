from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError, IntegerField
from wtforms.validators import DataRequired

class Search(FlaskForm):
	location = StringField('Location', validators=[DataRequired()])
	rooms = StringField('No. of Rooms', validators=[DataRequired()])
	submit = SubmitField('Search')