from Vehicle import Vehicle
import csv

class Customer:
    def __init__(self, name, c_score, location, contact):
        self.name = name
        self.c_score = c_score
        self.location = location
        self.contact = contact

    def request_rent(self):
        print("Available Vehicles:")
        for i, v in enumerate(Vehicle.vehicle_list):
            if v.is_available:
                print(f"{i+1}. {v.name}, Rent: {v.r_cost}")

        choice = int(input("Select a vehicle by number: ")) - 1
        rental_days = int(input("Enter rental duration (days): "))

        selected_vehicle = Vehicle.vehicle_list[choice]
        total_cost = selected_vehicle.r_cost * rental_days
        print(f"Total Cost: {total_cost}")
        
        payment = input("Confirm payment? (yes/no): ").lower()
        if payment == 'yes':
            selected_vehicle.authorize_rent()
        else:
            print("Payment not confirmed. Rental cancelled.")

    @classmethod
    def load_customers_from_csv(cls, file_path):
        customers = []
        with open('C:/Users/nayan/OneDrive/Desktop/DSA,ML,Python/Python_Projects/Vehicle_Registration_System/users.csv', 'r') as f:
            reader = csv.DictReader(f)
            for user in reader:
                customers.append(
                    cls(
                        name=user['name'],
                        c_score=user['c_score'],
                        location=user['location'],
                        contact=user['contact']
                    )
                )
        return customers

    def initiate_return(self, vehicle_name):
        for v in Vehicle.vehicle_list:
            if v.name == vehicle_name and not v.is_available:
                v.accept_return()
                return
        print("No such rented vehicle found.")
