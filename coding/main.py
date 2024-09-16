from flask import Flask, request, redirect, url_for, session, render_template
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
from database import init_db  # Import the init_db function

app = Flask(__name__)
app.secret_key = 'yellow'

# Initialize database
init_db()

# Database connection
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        conn = get_db_connection()
        flights = conn.execute('SELECT * FROM flights').fetchall()
        conn.close()
        return render_template('home.html', username=username, flights=flights)
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()

        if user and check_password_hash(user['password'], password):
            session['username'] = username
            session['account_type'] = user['account_type']
            return redirect(url_for('index'))
        return 'Invalid username or password'

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        account_type = request.form['account_type']  # admin or user

        conn = get_db_connection()
        try:
            conn.execute('INSERT INTO users (username, password, account_type) VALUES (?, ?, ?)',
                         (username, password, account_type))
            conn.commit()
        except sqlite3.IntegrityError:
            return 'Username already exists'
        finally:
            conn.close()

        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('account_type', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
