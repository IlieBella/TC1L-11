from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Userprofile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(1000), unique=True, nullable=False)
    name = db.Column(db.String(1000), nullable=False)
    email = db.Column(db.String(1000), nullable=False)
    phonenumber = db.Column(db.Integer, nullable=False)
    emergencyphonenumber = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Userprofile('{self.username}', '{self.name}')"