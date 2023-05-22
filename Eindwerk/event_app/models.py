from . import db
from datetime import datetime
from flask_login import UserMixin
from sqlalchemy.sql import func




class Task(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Text, nullable=False)
    note = db.Column(db.Text, nullable=True)
    priority = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.Date, default=datetime.date(datetime.now()))
    deadline = db.Column(db.Date, nullable=True)
    status = db.Column(db.String(30))

   


class User(db.Model, UserMixin):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    tasks = db.relationship('Task')


class Event(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(150), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    budget = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)
    program = db.Column(db.String(150), nullable=False)
    category = db.Column(db.String(30))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Meeting(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(150), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), )

    
    
class Stakeholder(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(150))
    phone_number = db.Column(db.Integer)
    type = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    company = db.Column(db.String(45))

   
    

    
