from Vehicle import Vehicle
from Customer import Customer

def main():
    # Load data from CSV files
    Vehicle.load_vehicles_from_csv("vehicles.csv")
    customers = Customer.load_customers_from_csv("users.csv")

    print("Welcome to the Vehicle Rental System!")
    
    while True:
        print("\n1. View Available Vehicles\n2. Rent a Vehicle\n3. Return a Vehicle\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            Vehicle.show_available_vehicles()
        elif choice == "2":
            customer_name = input("Enter your name: ")
            customer = next((c for c in customers if c.name == customer_name), None)
            if customer:
                customer.request_rent()
            else:
                print("Customer not found!")
        elif choice == "3":
            vehicle_name = input("Enter the name of the vehicle to return: ")
            customer_name = input("Enter your name: ")
            customer = next((c for c in customers if c.name == customer_name), None)
            if customer:
                customer.initiate_return(vehicle_name)
            else:
                print("Customer not found!")
        elif choice == "4":
            print("Thank you for using the Vehicle Rental System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
