import csv

class Vehicle:
    vehicle_list = []  # Class-level list to store all vehicle objects

    def __init__(self, name, r_cost, tyre_count, is_available):
        self.name = name
        self.r_cost = r_cost
        self.tyre_count = tyre_count
        self.is_available = is_available
        Vehicle.vehicle_list.append(self)  # Automatically adds the instance to the list

    def authorize_rent(self):
        self.is_available = False
        print(f"The vehicle {self.name} has been rented successfully.")

    def accept_return(self):
        self.is_available = True
        print(f"The vehicle {self.name} has been returned and is now available.")

    @staticmethod
    def show_available_vehicles():
        print("Available Vehicles:")
        for v in Vehicle.vehicle_list:
            if v.is_available:
                print(f"{v.name}, Rent: {v.r_cost}, Tyres: {v.tyre_count}")

    @classmethod
    def load_vehicles_from_csv(cls, file_path):
        with open('C:/Users/nayan/OneDrive/Desktop/DSA,ML,Python/Python_Projects/Vehicle_Registration_System/vehicles.csv', 'r') as f:
            reader = csv.DictReader(f)
            for vehicle in reader:
                cls(
                    name=vehicle['name'],
                    r_cost=float(vehicle['r_cost']),
                    tyre_count=int(vehicle['tyre_count']),
                    is_available=vehicle['is_available'] == "True"
                )
