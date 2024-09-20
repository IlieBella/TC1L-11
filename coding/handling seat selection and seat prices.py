from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class PrivateJetTicketingSystem:
    def __init__(self):
        # Define a simple plane layout with 'W' as window seats, 'A' as aisle seats, and 'X' as booked seats
        self.plane_layout = [
            ['W', 'A', 'A', 'W'],
            ['W', 'A', 'A', 'W'],
            ['W', 'A', 'A', 'W'],
            ['W', 'A', 'A', 'W'],
        ]
        # Set prices for window and aisle seats in RM
        self.seat_prices = {
            'W': 500,  # Window seat price in RM
            'A': 400   # Aisle seat price in RM
        }
    
    def display_plane_layout(self):
        print("Current Plane Layout (W: Window, A: Aisle, X: Booked):")
        for row in self.plane_layout:
            print(" ".join(row))
        print()  # For spacing

    def get_seat_price(self, seat_type):
        return self.seat_prices.get(seat_type, 0)

    def select_seat(self, row, col):
        if self.plane_layout[row][col] == 'X':
            print("Seat is already booked. Please choose another seat.")
            return False
        else:
            seat_type = self.plane_layout[row][col]
            price = self.get_seat_price(seat_type)
            print(f"Seat selected: {seat_type} seat, Price: RM {price}")
            confirm = input("Do you want to book this seat? (yes/no): ").lower()
            if confirm == 'yes':
                self.plane_layout[row][col] = 'X'  # Mark seat as booked
                print("Seat booked successfully!")
                return True
            else:
                print("Seat booking canceled.")
                return False

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


# Main Program Execution
if __name__ == "__main__":
    system = PrivateJetTicketingSystem()
    system.start_booking()




#seat icon
#https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pikpng.com%2Fpngvi%2FwowRiJ_flight-seat-filled-icon-airplane-seat-icon-clipart%2F&psig=AOvVaw2nAp566lyO-3AkMd_bZgmO&ust=1726202630528000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCJia-IfMvIgDFQAAAAAdAAAAABAE
