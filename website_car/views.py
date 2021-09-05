from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
# from .models import Note
# from . import db
# import json

views = Blueprint('views', __name__)

@views.route('/contact_us')
def contact_us():
    return render_template("contact_us.html", user=current_user)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)



