from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Selection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flightid = db.Column(db.String(1000), unique=True, nullable=False)
    departuredate = db.Column(db.Date(), nullable=False)
    destination = db.Column(db.String(1000), nullable=False)
    date_posted = db.Column(db.DateTime(timezone=True), nullable=False, default=func.now())

    def __repr__(self):
        return f"Selection('{self.flightid}', '{self.departuredate}')"
        