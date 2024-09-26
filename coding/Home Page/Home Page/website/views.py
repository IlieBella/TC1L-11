from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import Selection

views = Blueprint('views', __name__)

@views.route('/', methods=['get', 'post'])
def home():
    if request.method == 'post':
        flightid = request.form.get(flightid)
        departuredate = request.form.get(departuredate)
        destination = request.form.get(destination)
    else:
        new_selection = Selection(flightid=flightid, departuredate=departuredate, destination=destination)
        db.session.add(new_selection)
        db.session.commit()
        return redirect(url_for('/')) #plane seat layout url    

    return render_template("home.html", user=current_user)