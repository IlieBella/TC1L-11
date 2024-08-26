from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'a_random_secret_key'  # Replace with a real secret key

# Sample user data (username: password)
users = {
    'user1': 'password',
    'user2': 'password2',
}

@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users and users[username] == password:
            session['username'] = username
            flash('Login successful!')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password!')
    
    return render_template('login.html')

@app.route('/logout')

def logout():
    if 'username' in session:
        flash(f"Goodbye, {session['username']}!")
        session.pop('username', None)
    else:
        flash("No user is currently logged in.")
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
