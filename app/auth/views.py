import flask_uploads

from app.main.forms import ProfileUpdate
from flask import render_template, flash, redirect, request, url_for
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.utils import secure_filename
from ..mail import sendmail

from . import auth
from ..models import Pitch, User
from .forms import UserRegistration, UserLogin
from .. import db, photos


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = UserRegistration()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    bio=form.bio.data,
                    password=form.password.data,
                    img='/img/user.jpg')
        db.session.add(user)
        db.session.commit()
        sendmail("Welcome to PitchApp",
                 "email/welcome_user",
                 user.email,
                 user=user)
        return redirect(url_for('auth.login'))
    title = "New Account"
    return render_template('auth/register.html',
                           registratration_form=form,
                           title=title)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    loginform = UserLogin()
    if loginform.validate_on_submit():
        user = User.query.filter_by(email=loginform.email.data).first()
        if user is not None and user.passwordVerification(
                loginform.password.data):
            login_user(user, loginform.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid Credentials!')
    title = "User Login"
    return render_template('auth/login.html',
                           login_form=loginform,
                           title=title)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@auth.route('/profile')
@login_required
def profile():
    
    pitch=Pitch.query.filter_by(owner=current_user.username).all()
    title = "Profile"
    print(current_user.username)
    
    return render_template('auth/profile.html', title=title,item=pitch)


@auth.route('/profile/update', methods=['POST', 'GET'])
@login_required
def updateuser():
    form = ProfileUpdate()
    if form.validate_on_submit():
        user = User.query.filter_by(username=current_user.username).first()
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

    return render_template('auth/update.html', form=form)


@auth.route('/profile/update/pic', methods=['POST', 'GET'])
@login_required
def upload():
    name = current_user.username
    user = User.query.filter_by(username=name).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'img{filename}'
        user.img = path
        db.session.commit()
        redirect(url_for('main.index'))
