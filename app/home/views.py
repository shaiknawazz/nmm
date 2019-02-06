from flask import abort, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required

#Preceding dots represents the going backward in dirs.
from .. import db
from ..models import Users, Properties, Enquiries
from .forms import Search
#Imports home from __init__.py file in home directory
from . import home

@home.route('/')
@home.route('/index')
def index():
	form = Search()
	return render_template('home/search.html', form=form, current_user=current_user)

@home.route('/results', methods=['GET','POST'])
def results():
	form = Search()
	if form.validate_on_submit():
		rooms = form.rooms.data
		properties = Properties.query.filter_by(rooms=int(rooms)).all()
		return render_template('home/results.html', current_user=current_user, properties=properties)

@home.route('/newenquiry/<property_id>')
@login_required
def new_enquiry(property_id):
	enquiry = Enquiries(property_id=property_id,
						enquirer_id=current_user.user_id)
	db.session.add(enquiry)
	db.session.commit()
	flash('Enquiry Created Successfully')
	return redirect(url_for('home.custom_property_home',property_id=property_id,
					user=current_user.user_id))

@home.route('/homeproperty/<user>/<property_id>')
def custom_property_home(user, property_id):
	property_details = Properties.query.get(property_id)
	return render_template('home/property_details.html',property=property_details)

@home.route('/userenquiries')
@login_required
def user_enquiries():
	user = Users.query.get(current_user.user_id)
	enquiries = user.user_enquiries
	return render_template('tenant/uenquiries.html', enquiries=enquiries)

@home.route('/services')
def services():
	return render_template('services.html')

@home.route('/about')
def about():
	return render_template('property.html')

@home.route('/contact', methods=['GET','POST'])
def contact():
	return render_template('home/contact.html')