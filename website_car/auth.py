from flask import Blueprint, render_template, redirect, request, flash, redirect, url_for
from . import models, db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

# Login Function
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password1')

        user = models.User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect username or password.', category='error')
        else:
            flash('User does not exist', category='error')

    return render_template("login.html", user=current_user)

#  Logout Function
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

#  Sign Up Function
@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':

        email_address = request.form.get('email_address')
        full_name = request.form.get('full_name')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = models.User.query.filter_by(email_addr=email_address).first()

        if user:
            flash('Email already exists.', category='error')
        elif models.User.query.filter_by(username=username).first():
            flash('Username already exists.', category='error')
        elif len(email_address) < 5:
            flash("Email must have over 5 characters.", category='error')
        elif len(full_name) < 6:
            flash("Full name must have over 2 characters.", category='error')
        elif len(username) < 2:
            flash("Username must have over than 6.", category='error')
        elif password1 != password2:
            flash("Password does not match.", category='error')
        elif len(password1) < 7:
            flash("Password must be greater than 7 words.", category='error')
        else:
            new_user = models.User(
                email_addr=email_address,
                full_name=full_name,
                username=username,
                password=generate_password_hash(password1, method='sha256')
                )
            db.session.add(new_user)
            db.session.commit()
            flash('Account Created!', category='success')
            return redirect(url_for('auth.login'))

    return render_template("sign_up.html", user=current_user)