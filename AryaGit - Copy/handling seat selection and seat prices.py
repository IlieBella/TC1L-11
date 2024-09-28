from flask import Flask, request, redirect, url_for, session, render_template, flash
from flask_login import current_user
import sqlite3
from database import init_db
from forms import UpdateProfileForm

app = Flask(__name__)
app.secret_key = 'yellow'

init_db()

plane_layout = [
    ['W', 'A', 'A', 'W'],
    ['W', 'A', 'A', 'W'],
    ['W', 'A', 'A', 'W'],
    ['W', 'A', 'A', 'W'],
]
seat_prices = {
    'W': 500,  
    'A': 400   
}

class PrivateJetTicketingSystem:
    def __init__(self):
        self.plane_layout = plane_layout
        self.seat_prices = seat_prices

    def display_plane_layout(self):
        print("Current Plane Layout (W: Window, A: Aisle, X: Booked):")
        for row in self.plane_layout:
            print(" ".join(row))
        print()  

    def select_seat(self, row, col):
        if self.plane_layout[row][col] == 'X':
            print("Seat is already booked. Would you like to unselect this seat? (yes/no): ", end='')
            confirm = input().strip().lower()
            if confirm == 'yes':
                self.unselect_seat(row, col)
                return False  
            else:
                return False  

        else:
            seat_type = self.plane_layout[row][col]
            price = self.seat_prices[seat_type]
            print(f"Seat selected: {seat_type} seat, Price: RM {price}")
            print("Do you want to book this seat? (yes/no): ", end='')
            confirm = input().strip().lower()
            if confirm == 'yes':
                self.plane_layout[row][col] = 'X'  
                print("Seat booked successfully!")
                return True  
            else:
                print("Seat booking canceled.")
                return False

    def unselect_seat(self, row, col):
        if self.plane_layout[row][col] == 'X':
            seat_type = 'W' if (col == 0 or col == 3) else 'A'  
            self.plane_layout[row][col] = seat_type  
            print("Seat unbooked successfully!")
        else:
            print("This seat is not booked.")

    def start_booking(self):
        while True:
            self.display_plane_layout()
            row = int(input("Enter the row number (0-3): "))
            col = int(input("Enter the column number (0-3): "))
            
            if row in range(4) and col in range(4):
                if self.select_seat(row, col):
                    break  
            else:
                print("Invalid seat selection. Please try again.")
        
        print("Thank you for using LUXURAIR!")

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
