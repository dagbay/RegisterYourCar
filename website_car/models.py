from datetime import timezone
from enum import unique
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)

    email_addr = db.Column(db.String(255), unique=True)
    full_name = db.Column(db.String(255))
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    vehicles = db.relationship('Vehicle')

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    rego = db.Column(db.String(255), unique=True)
    make = db.Column(db.String(255))
    model = db.Column(db.String(255))
    info = db.Column(db.String(255))
    date = db.Column(db.DateTime(timezone=True), default=func.now())

