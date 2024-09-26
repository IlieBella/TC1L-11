from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import Userprofile

views = Blueprint('views', __name__)

@views.route('/userprofile', methods=['get', 'post'])
def userprofile():
    if request.method == 'post':
        username = request.form.get(username)
        name = request.form.get(name)
        email = request.form.get(email)
        phonenumber = request.form.get(phonenumber)
        emergencyphonenumber = request.form.get(emergencyphonenumber)
    else:
        new_userprofile = Userprofile(username=username, name=name, email=email, phonenumber=phonenumber, emergencyphonenumber=emergencyphonenumber)
        db.session.add(new_userprofile)
        db.session.commit()
        return redirect(url_for('/')) 

    return render_template("userprofile.html", user=current_user)