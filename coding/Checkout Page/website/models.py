from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Checkout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(10000), nullable=False)
    lastname = db.Column(db.String(10000), nullable=False)
    country = db.Column(db.String(1000), nullable=False)
    city = db.Column(db.String(1000), nullable=False)
    zipcode = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(1000), unique=True, nullable=False)
    phonenumber = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Checkout('{self.firstname}', '{self.lastname}')"