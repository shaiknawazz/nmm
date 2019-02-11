from flask import flash, redirect, render_template, url_for, request
from flask_login import login_required, login_user, logout_user

from .. import db
from ..models import Users
from .forms import LoginForm, RegistrationForm, CompleteProfileForm
from . import auth


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(mobile_no=form.mobile_no.data).first()
        if user is not None and user.verify_password(form.password.data):
            if login_user(user):
                return redirect(url_for('home.dashboard'))
        else:
            flash('Invalid email or password.')
    return render_template('auth/login.html', form=form)


@auth.route('/completeProfile', methods=['GET', 'POST'])
@login_required
def completeProfile():
    form = CompleteProfileForm()
    if request.method == 'POST':
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.here')
        return redirect(url_for('home.dashboard'))

    return render_template('auth/completeProfile.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Users(email=form.email.data,
                     name=form.name.data,
                     user_type=form.user_type.data,
                     mobile_no=form.mobile_no.data,
                     password=form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('auth.completeProfile'))
        # flash('Successfully Registered')
        # return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have successfully been logged out.')
    return redirect(url_for('auth.login'))
