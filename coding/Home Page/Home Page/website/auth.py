from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, logout_user, current_user
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/logout')
def logout():
    return redirect(url_for('')) #login page url