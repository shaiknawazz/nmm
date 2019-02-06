from flask import request
from flask_restful import Api, Resource, abort
from . import api, rest
from .. import db
from ..models import *

def cal_rent(a):
	return a*5

class Login(Resource):
	#For login
	def post(self):
		mobile_no = request.form['mobile_no']
		password = request.form['password']
		user_details = {}
		user = Users.query.filter_by(mobile_no=mobile_no).first()
		if user is not None and user.verify_password(password):
			user_details['user_id'] = user.user_id
			user_details['email'] = user.email
			user_details['mobile_no'] = user.mobile_no
			user_details['name'] = user.name
			user_details['user_type'] = user.user_type
			return user_details,201
		else:
			return abort(404, message="User {} doesn't exist".format(mobile_no))

class Register(Resource):
	#For Register
	def post(self):
		name = request.form['name']
		email = request.form['email']
		mobile_no = request.form['mobile_no']
		password = request.form['password']
		user_type = request.form['user_type']
		user = Users(email = email,
					name=name,
					user_type=user_type,
					mobile_no = mobile_no,
                    password=password)
		if Users.query.filter_by(email=email).first() and Users.query.filter_by(mobile_no=mobile_no).first():
			return {'status':'0','message':'User Already Exists'},404
		else :
			db.session.add(user)
			db.session.commit()
			return {'status':'1','message':'User Successfully Registered'},201

class Property(Resource):
	#For properties
	def post(self):
		property_name = request.form['property_name']
		address = request.form['address']
		rooms = request.form['rooms']
		landlord_id = request.form['landlord_id']
		rent = cal_rent(5)
		property = Properties(property_name=property_name,
							  address=address,
							  rent=rent,
							  rooms=rooms,
							  landlord=landlord_id)
		db.session.add(property)
		db.session.commit()

		return {'calculates_rent':rent},201

class Enquiry(Resource):
	#For enquiries
	def post(self):
		property_id = request.form['property_id']
		enquirer_id = request.form['enquirer_id']

		enquiry = Enquiries(property_id=property_id,
							enquirer_id=enquirer_id)

		db.session.add(enquiry)
		db.session.commit()

		return {'Status':'Done'},201

rest.add_resource(Login, '/login')
rest.add_resource(Register, '/register')
rest.add_resource(Property, '/addproperty')
rest.add_resource(Enquiry, '/enquiry')