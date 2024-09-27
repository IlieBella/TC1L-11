from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class PrivateJetTicketingSystem:
    flights_data = {
    'PJ101': {
        'plane_layout': [
            ['W', 'A', 'A', 'W'],
            ['W', 'A', 'A', 'W'],
            ['W', 'A', 'A', 'W'],
            ['W', 'A', 'A', 'W']
        ],
        'seat_prices': {'W': 500, 'A': 400}
    },
    'PJ102': {
        'plane_layout': [
            ['W', 'A', 'W', 'W'],
            ['W', 'A', 'W', 'W'],
            ['W', 'A', 'A', 'W'],
            ['W', 'A', 'A', 'W']
        ],
        'seat_prices': {'W': 600, 'A': 450}
    },
    'PJ103': {
        'plane_layout': [
            ['W', 'W', 'A', 'A'],
            ['W', 'W', 'A', 'A'],
            ['A', 'A', 'W', 'W'],
            ['A', 'A', 'W', 'W']
        ],
        'seat_prices': {'W': 700, 'A': 500}
    },
    'PJ104': {
        'plane_layout': [
            ['W', 'A', 'A', 'W'],
            ['W', 'A', 'A', 'W'],
            ['A', 'W', 'W', 'A'],
            ['A', 'W', 'W', 'A']
        ],
        'seat_prices': {'W': 550, 'A': 450}
    },
    'PJ105': {
        'plane_layout': [
            ['W', 'A', 'A', 'W'],
            ['W', 'A', 'A', 'W'],
            ['W', 'A', 'A', 'W'],
            ['W', 'A', 'A', 'W']
        ],
        'seat_prices': {'W': 650, 'A': 500}
    },
    'PJ106': {
        'plane_layout': [
            ['W', 'A', 'W', 'A'],
            ['W', 'A', 'A', 'W'],
            ['W', 'A', 'A', 'W'],
            ['A', 'W', 'A', 'W']
        ],
        'seat_prices': {'W': 800, 'A': 600}
    },
    'PJ107': {
        'plane_layout': [
            ['W', 'A', 'A', 'W'],
            ['A', 'A', 'W', 'W'],
            ['A', 'W', 'W', 'A'],
            ['A', 'A', 'W', 'W']
        ],
        'seat_prices': {'W': 1000, 'A': 700}
    },
    'PJ108': {
        'plane_layout': [
            ['W', 'W', 'A', 'A'],
            ['A', 'A', 'W', 'W'],
            ['A', 'A', 'W', 'W'],
            ['W', 'W', 'A', 'A']
        ],
        'seat_prices': {'W': 750, 'A': 550}
    },
    'PJ109': {
        'plane_layout': [
            ['W', 'A', 'W', 'A'],
            ['W', 'A', 'W', 'A'],
            ['A', 'W', 'A', 'W'],
            ['A', 'A', 'W', 'W']
        ],
        'seat_prices': {'W': 900, 'A': 600}
    },
    'PJ110': {
        'plane_layout': [
            ['W', 'A', 'A', 'W'],
            ['W', 'A', 'A', 'W'],
            ['A', 'W', 'A', 'W'],
            ['A', 'A', 'W', 'W']
        ],
        'seat_prices': {'W': 950, 'A': 700}
     },

    'PJ111': {
        'plane_layout': [
            ['W', 'A', 'A', 'W'],
            ['A', 'A', 'W', 'W'],
            ['W', 'A', 'A', 'W'],
            ['A', 'A', 'W', 'W']
        ],
        'seat_prices': {'W': 550, 'A': 400}
    },
    'PJ112': {
        'plane_layout': [
            ['W', 'A', 'W', 'A'],
            ['W', 'A', 'A', 'W'],
            ['W', 'A', 'A', 'W'],
            ['A', 'W', 'A', 'W']
        ],
        'seat_prices': {'W': 600, 'A': 450}
    },
    'PJ113': {
        'plane_layout': [
            ['W', 'A', 'A', 'W'],
            ['A', 'A', 'W', 'W'],
            ['A', 'W', 'A', 'A'],
            ['W', 'A', 'W', 'A']
        ],
        'seat_prices': {'W': 750, 'A': 500}
    },
    'PJ114': {
        'plane_layout': [
            ['W', 'W', 'A', 'A'],
            ['W', 'A', 'A', 'W'],
            ['A', 'W', 'A', 'A'],
            ['A', 'W', 'W', 'A']
        ],
        'seat_prices': {'W': 600, 'A': 450}
    },
    'PJ115': {
        'plane_layout': [
            ['W', 'A', 'A', 'W'],
            ['A', 'A', 'W', 'W'],
            ['W', 'A', 'A', 'W'],
            ['A', 'W', 'W', 'A']
        ],
        'seat_prices': {'W': 500, 'A': 400}
    },
    'PJ116': {
        'plane_layout': [
            ['W', 'A', 'A', 'W'],
            ['A', 'A', 'W', 'W'],
            ['A', 'W', 'A', 'A'],
            ['W', 'A', 'W', 'A']
        ],
        'seat_prices': {'W': 550, 'A': 450}
    },
    'PJ117': {
        'plane_layout': [
            ['W', 'A', 'A', 'W'],
            ['A', 'A', 'W', 'W'],
            ['A', 'W', 'A', 'W'],
            ['W', 'A', 'A', 'W']
        ],
        'seat_prices': {'W': 650, 'A': 500}
    },
    'PJ118': {
        'plane_layout': [
            ['W', 'A', 'A', 'W'],
            ['W', 'A', 'W', 'A'],
            ['A', 'W', 'A', 'A'],
            ['A', 'W', 'W', 'A']
        ],
        'seat_prices': {'W': 700, 'A': 550}
    },
    'PJ119': {
        'plane_layout': [
            ['W', 'A', 'A', 'W'],
            ['A', 'W', 'W', 'A'],
            ['W', 'A', 'A', 'W'],
            ['A', 'W', 'W', 'A']
        ],
        'seat_prices': {'W': 750, 'A': 600}
    },
    'PJ120': {
        'plane_layout': [
            ['W', 'A', 'A', 'W'],
            ['A', 'A', 'W', 'W'],
            ['W', 'A', 'A', 'W'],
            ['A', 'W', 'A', 'A']
        ],
        'seat_prices': {'W': 800, 'A': 650}
    }
}


    def display_plane_layout(self):
        print("Current Plane Layout (W: Window, A: Aisle, X: Booked):")
        for row in self.plane_layout:
            print(" ".join(row))
        print()  # For spacing

    def select_seat(self, row, col):
        if self.plane_layout[row][col] == 'X':
            print("Seat is already booked. Would you like to unselect this seat? (yes/no): ", end='')
            confirm = input().strip().lower()
            if confirm == 'yes':
                self.unselect_seat(row, col)
                return False  # Indicates unselection, not booking
            else:
                return False  # Not booking

        else:
            seat_type = self.plane_layout[row][col]
            price = self.seat_prices[seat_type]
            print(f"Seat selected: {seat_type} seat, Price: RM {price}")
            print("Do you want to book this seat? (yes/no): ", end='')
            confirm = input().strip().lower()
            if confirm == 'yes':
                self.plane_layout[row][col] = 'X'  # Mark seat as booked
                print("Seat booked successfully!")
                return True  # Indicates successful booking
            else:
                print("Seat booking canceled.")
                return False

    def unselect_seat(self, row, col):
        if self.plane_layout[row][col] == 'X':
            seat_type = 'W' if (col == 0 or col == 3) else 'A'  # Determine original seat type
            self.plane_layout[row][col] = seat_type  # Unmark the seat as booked
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
                    break  # Exit after a successful booking
            else:
                print("Invalid seat selection. Please try again.")
        
        print("Thank you for using LUXURAIR!")

# Main Program Executionpyt
if __name__ == "__main__":
    system = PrivateJetTicketingSystem()
    system.start_booking()
