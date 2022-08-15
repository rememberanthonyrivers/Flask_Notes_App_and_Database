# this file is used to store all database models
from . import db    #
from flask_login import UserMixin   #   module that helps our user login   
from sqlalchemy.sql import func     #   sql alchemy is handeling the date and time 
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    # with each new note object, the software will auto increment by one 
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))   #   type of column is an integer 
class User(db.Model,UserMixin):  #  lets define our users attributes below --\/-- everyonoe will have an id, email, password, first name
    id = db.Column(db.Integer, primary_key=True)    #   unique identifier for our variable object
    email = db.Column(db.String(150), unique=True)  #   sting bif with max char amount / unique makes it so every user has a unique solo value 
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')