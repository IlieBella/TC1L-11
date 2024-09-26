from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import Checkout

views = Blueprint('views', __name__)

@views.route('/checkout', methods=['get', 'post'])
def checkout():
    if request.method == 'post':
        firstname = request.form.get(firstname)
        lastname = request.form.get(lastname)
        country = request.form.get(country)
        city = request.form.get(city)
        zipcode = request.form.get(zipcode)
        email = request.form.get(email)
        phonenumber = request.form.get(phonenumber)
    else:
        new_checkout = Checkout(firstname=firstname, lastname=lastname, country=country, city=city, zipcode=zipcode, email=email, phonenumber=phonenumber)
        db.session.add(new_checkout)
        db.session.commit()
        return redirect(url_for('/'))    

    return render_template("checkout.html", user=current_user)
