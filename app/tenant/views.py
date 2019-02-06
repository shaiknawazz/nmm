from flask_login import current_user, login_required
from flask import abort, render_template, flash, redirect, url_for, request
import json

from .. import db
from ..models import Enquiries, Properties, Users
from . import tenant
from .forms import *

'''All the routes that render webpages.'''

#List of properties user enquired for
@tenant.route('/userenquiries')
@login_required
def user_enquiries():
	user = Users.query.get(current_user.user_id)
	enquiries = user.user_enquiries
	return render_template('tenant/uenquiries.html', enquiries=enquiries)