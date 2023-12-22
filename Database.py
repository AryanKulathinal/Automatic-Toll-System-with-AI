import sqlite3

class Database:

    def __init__(self) -> None:

        self.conn = sqlite3.connect('vehicle_database.db')

        # Create a cursor object to execute SQL queries
        self.cursor = self.conn.cursor()

        # Create a table to store vehicle details
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS vehicles (
                vehicle_number TEXT PRIMARY KEY,
                name TEXT,
                phone_number TEXT,
                state TEXT,
                type TEXT,
                address TEXT
            )
        ''')
        
    def add_vehicle(self, vehicle_number, name, phone_number, state, type, address):
        try:
            self.cursor.execute('''
                INSERT INTO vehicles (vehicle_number, name, phone_number, state, type, address)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (vehicle_number, name, phone_number, state, type, address))
            self.conn.commit()
            print(f"Vehicle {vehicle_number} details added to the database.")
        except sqlite3.IntegrityError:
            print("Vehicle number already exists in the database.")

    def display_vehicle_details(self, vehicle_number):
        self.cursor.execute('SELECT * FROM vehicles WHERE vehicle_number = ?', (vehicle_number,))
        result = self.cursor.fetchone()
        if result:
            print(f"Vehicle Number: {result[0]}")
            print(f"Name: {result[1]}")
            print(f"Phone Number: {result[2]}")
            print(f"State: {result[3]}")
            print(f"Type: {result[4]}")
            print(f"Address: {result[5]}")
            return True
        else:
            # print(f"Vehicle {vehicle_number} not found in the database.")
            return False
    def get_type(self, vehicle_number):
        self.cursor.execute('SELECT type FROM vehicles WHERE vehicle_number = ?', (vehicle_number,))
        result = self.cursor.fetchone()
        return result[0]


if __name__ == "__main__":

    D = Database()
    # D.add_vehicle('ABC123', 'John Doe', '1234567890', "New York", '123 Main St')
    # D.add_vehicle('XYZ789', 'Jane Smith', '9876543210', "New York", '456 Oak St')
    # D.display_vehicle_details('ABC123')
    # D.display_vehicle_details('XYZ789')
    # D.display_vehicle_details('123XYZ')
    # D.add_vehicle("R-183-JF" , "Radu Dragomir", "+40 721 123 456", "Romania", "Car", "Bucharest, Romania")
    # D.add_vehicle("N-894-JV" , "Nina Bjornsen", "+47 912 345 678", "Norway", "Car", "Oslo, Norway")
    # D.add_vehicle("L-656-XH" , "Lucas Müller", "+352 621 987 654", "Luxembourg", "Car", "Luxembourg City, Luxembourg")
    # D.add_vehicle("H-644-LX" , "Hedvig Kovács", "+36 30 876 5432", "Hungary", "Car", "Budapest, Hungary")

    D.display_vehicle_details('R-183-JF')
    D.display_vehicle_details('L-656-XH')
    D.display_vehicle_details('H-644-LX')

    D.get_type("R-183-JF")