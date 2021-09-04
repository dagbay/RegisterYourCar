import re
from flask import Blueprint, render_template, redirect, request, flash, redirect, url_for
# from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
# from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return redirect('/')

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email_addr = request.form.get('email_addr')
        full_name = request.form.get('full_name')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if email_addr < 5:
            flash("Email must be greater than 5 characters.", category='error')
        elif username < 6:
            flash("Username is too short.", category='error')
        elif len(full_name) < 2:
            pass
        elif password1 != password2:
            pass
        elif len(password1) < 7:
            pass
        else:
            # add to database
            pass

    return render_template("sign_up.html")