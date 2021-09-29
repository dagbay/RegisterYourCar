from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
import smtplib
from werkzeug.security import generate_password_hash, check_password_hash
from . import models, db

# Set views as a blueprint for use in other python files.
views = Blueprint('views', __name__)

# Function for the index page
@views.route('/')
def index():
    return render_template("index.html", user=current_user)

# Function for the contact us page
@views.route('/contact_us', methods=['GET', 'POST'])
def contact_us():

    if request.method == 'POST':
        sender_email = 'danieljoremen123456789@gmail.com'
        password = 'VixenNoodle2012'
        message = request.form.get('note')
        server = smtplib.SMTP('smtp.gmail.com', 587)

        rec_email = current_user.email_addr
        print(rec_email)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, rec_email, message)
        return redirect(url_for('views.dashboard'))

    return render_template("contact_us.html", user=current_user)

# Function for the dashboard page
@views.route('/dashboard')
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user)

# Function for the register vehicle page
@views.route('/register_vehicle', methods=['GET', 'POST'])
@login_required
def register_vehicle():

    if request.method == 'POST':
        make = request.form.get('make')
        model = request.form.get('model')

        new_vehicle = models.Vehicle(
                make = make,
                model = model,
                user_id = current_user.id
                )
        db.session.add(new_vehicle)
        db.session.commit()
        flash('Vehicle Registered!', category='success')
    
    return render_template("register_vehicle.html", user=current_user)

# Function for the profile page which can only be accessed when the user is logged in.
@views.route('/profile')
@login_required
def profile():
    return render_template("profile.html", user=current_user)

# Function for the your vehicles page which can only be accessed when the user is logged in.
@views.route('/your_vehicles')
@login_required
def your_vehicles():
    return render_template("your_vehicles.html", user=current_user)