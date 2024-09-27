from flask import render_template, url_for, flash, redirect, request
from flask_login import login_required, current_user, login_user, logout_user
from main import app, db
from models import User
from forms import UpdateProfileForm
from werkzeug.security import generate_password_hash, check_password_hash

@app.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    form = UpdateProfileForm()
    if form.validate_on_submit():
        # Update user profile
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('profile.html', title='Profile', image_file=image_file, form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

# Additional routes for login and registration should be added here

