from flask import Flask, request, redirect, url_for, session, render_template, flash
from flask_login import current_user
import sqlite3
from database import init_db
from forms import ChangeUsernameForm, ChangePasswordForm

app = Flask(__name__)
app.secret_key = 'yellow'

init_db()

plane_layout = [
    ['W', 'A', 'A', 'W'],
    ['W', 'A', 'A', 'W'],
    ['W', 'A', 'A', 'W'],
    ['W', 'A', 'A', 'W']
]

seat_prices = {
    'W': 500,
    'A': 400
}

def get_db_connection():
    conn = sqlite3.connect('luxurair.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'] 
        account_type = request.form['account_type']

        conn = get_db_connection()
        try:
            conn.execute('INSERT INTO users (username, password, account_type) VALUES (?, ?, ?)', 
                         (username, password, account_type))
            conn.commit()
            return redirect(url_for('login')) 
        except sqlite3.IntegrityError:
            return 'Username already exists'
        finally:
            conn.close()

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'] 

        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()

        if user and user['password'] == password:
            session['username'] = username
            session['account_type'] = user['account_type']
            return redirect(url_for('home'))  
        return 'Invalid username or password'

    return render_template('login.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/home')
def home():
    flights = [
        {"flight_number": "PJ101", "departure": "Kuala Lumpur", "arrival": "Singapore", "date": "2024-10-01", "time": "10:00"},
        {"flight_number": "PJ102", "departure": "Kuala Lumpur", "arrival": "Bangkok", "date": "2024-10-02", "time": "12:00"},
        {"flight_number": "PJ103", "departure": "Kuala Lumpur", "arrival": "Tokyo", "date": "2024-10-03", "time": "14:00"},
        {"flight_number": "PJ104", "departure": "Kuala Lumpur", "arrival": "Seoul", "date": "2024-10-04", "time": "16:00"},
        {"flight_number": "PJ105", "departure": "Kuala Lumpur", "arrival": "Sydney", "date": "2024-10-05", "time": "18:00"},
        {"flight_number": "PJ106", "departure": "Kuala Lumpur", "arrival": "London", "date": "2024-10-06", "time": "20:00"},
        {"flight_number": "PJ107", "departure": "Kuala Lumpur", "arrival": "New York", "date": "2024-10-07", "time": "22:00"},
        {"flight_number": "PJ108", "departure": "Kuala Lumpur", "arrival": "Dubai", "date": "2024-10-08", "time": "09:00"},
        {"flight_number": "PJ109", "departure": "Kuala Lumpur", "arrival": "Hong Kong", "date": "2024-10-09", "time": "11:00"},
        {"flight_number": "PJ110", "departure": "Kuala Lumpur", "arrival": "Los Angeles", "date": "2024-10-10", "time": "13:00"},
        {"flight_number": "PJ111", "departure": "Kuala Lumpur", "arrival": "Shanghai", "date": "2024-10-11", "time": "15:00"},
        {"flight_number": "PJ112", "departure": "Kuala Lumpur", "arrival": "Moscow", "date": "2024-10-12", "time": "17:00"},
        {"flight_number": "PJ113", "departure": "Kuala Lumpur", "arrival": "Mumbai", "date": "2024-10-13", "time": "19:00"},
        {"flight_number": "PJ114", "departure": "Kuala Lumpur", "arrival": "Bangkok", "date": "2024-10-14", "time": "21:00"},
        {"flight_number": "PJ115", "departure": "Kuala Lumpur", "arrival": "Phuket", "date": "2024-10-15", "time": "08:00"},
        {"flight_number": "PJ116", "departure": "Kuala Lumpur", "arrival": "Denpasar", "date": "2024-10-16", "time": "10:30"},
        {"flight_number": "PJ117", "departure": "Kuala Lumpur", "arrival": "Kota Kinabalu", "date": "2024-10-17", "time": "12:30"},
        {"flight_number": "PJ118", "departure": "Kuala Lumpur", "arrival": "Ho Chi Minh", "date": "2024-10-18", "time": "14:30"},
        {"flight_number": "PJ119", "departure": "Kuala Lumpur", "arrival": "Hanoi", "date": "2024-10-19", "time": "16:30"},
        {"flight_number": "PJ120", "departure": "Kuala Lumpur", "arrival": "Singapore", "date": "2024-10-20", "time": "18:30"},
    ]
    return render_template('home.html', flights=flights)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Handle the message (e.g., send an email, save to database, etc.)

        flash('Your message has been sent!', 'success')
        return redirect(url_for('home'))
    
    return render_template('contact.html')


@app.route('/user_profile', methods=['GET', 'POST'])
def profile():
    change_username_form = ChangeUsernameForm()
    change_password_form = ChangePasswordForm()

    # Check if the username change form is submitted
    if request.method == 'POST':
        if 'update_profile' in request.form and change_username_form.validate_on_submit():
            conn = get_db_connection()
            conn.execute('UPDATE users SET username = ? WHERE username = ?',
                         (change_username_form.username.data, session['username']))
            conn.commit()
            session['username'] = change_username_form.username.data  # Update session data with the new username
            conn.close()
            flash('Your username has been updated!', 'success')
            return redirect(url_for('profile'))

        # Check if the password change form is submitted
        elif 'change_password' in request.form and change_password_form.validate_on_submit():
            conn = get_db_connection()
            user = conn.execute('SELECT * FROM users WHERE username = ?', 
                                (session['username'],)).fetchone()

            # Check if the current password is correct
            if user and user['password'] == change_password_form.current_password.data:
                conn.execute('UPDATE users SET password = ? WHERE username = ?',
                             (change_password_form.new_password.data, session['username']))
                conn.commit()
                conn.close()
                flash('Your password has been updated!', 'success')
            else:
                flash('Current password is incorrect.', 'danger')

            return redirect(url_for('profile'))

    # Prepopulate the form with the current username on GET request
    if request.method == 'GET':
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', 
                            (session['username'],)).fetchone()
        conn.close()
        change_username_form.username.data = user['username']

    return render_template('userprofile.html', change_username_form=change_username_form, change_password_form=change_password_form)

@app.route('/booking')
def booking():
    selected_seat = session.get('selected_seat', None)
    seat_price = 0
    if selected_seat:
        row, col = map(int, selected_seat.split(','))
        seat_type = session.get('original_seat_type', {}).get(f'{row},{col}', plane_layout[row][col])
        if seat_type in seat_prices:
            seat_price = seat_prices[seat_type]

    return render_template('seat_selection.html', plane_layout=plane_layout, selected_seat=selected_seat, seat_price=seat_price, enumerate=enumerate)

@app.route('/confirm_booking', methods=['POST'])
def confirm_booking():
    seat_data = request.form.get('seat')
    
    if seat_data:
        row, col = map(int, seat_data.split(','))
        seat_type = session.get('original_seat_type', {}).get(seat_data, plane_layout[row][col])
        
        if plane_layout[row][col] == 'X':
            plane_layout[row][col] = seat_type
            flash(f'Seat at row {row+1}, column {col+1} has been unselected.', 'warning')
            session.pop('selected_seat', None)
        else:
            session.setdefault('original_seat_type', {})[seat_data] = seat_type
            plane_layout[row][col] = 'X'
            seat_price = seat_prices.get(seat_type, 0)
            session['selected_seat'] = seat_data
            flash(f'Success! You have booked seat {seat_type} at RM {seat_price}.', 'success')
        return redirect(url_for('booking')) 
    else:
        flash('No seat selected. Please select a seat.', 'danger')
        return redirect(url_for('booking'))

@app.route('/next_page')
def next_page():
    return "This is the next page after booking."

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('account_type', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)