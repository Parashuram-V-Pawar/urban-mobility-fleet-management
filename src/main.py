from electric_car import ElectricCar
from electric_scooter import ElectricScooter

# Main class
class EcoRideMain:

  # Empty dictionary to store hubs and vehicles
  fleet_hubs = dict()

  # Empty list to store the vehicle details
  vehicles = []

  # Function desplays a welcome message
  def greet(self):
    print("\nWelcome to Eco-Ride Urban Mobility System")



  # Function to add hub.
  def add_hub(self):
    hub_name = input("Enter hub name: ")
    if hub_name in self.fleet_hubs:
      print(f"Hub {hub_name} already present.")
    else:
      self.fleet_hubs[hub_name] = []
      print(f"{hub_name} was added successfully.")
    
    print(self.fleet_hubs)



  # Function to take vehicles inputs.
  def add_vehicles(self):
    hub_name = input("Enter hub name to add vehicles: ")
    if hub_name not in self.fleet_hubs:
      print(f"Hub {hub_name} is not present. Please add Hub first")
      return
    
    no_of_vehicles = int(input("Enter number of vehicles to add: \n"))
    for i in range(no_of_vehicles):
      print(f"Enter details for {i+1} vehicle")
      vehicle_id = input("Enter vehicle id: ")
      model = input("Enter vehicle model: ")
      battery_percentage = int(input("Enter available battery percentage: "))
      maintainance_status = input("Enter maintainance status(Available/ On Trip/ Under Maintainance): ")
      rental_price = int(input("Enter Rental price of the vehicle: "))

      vehicle_type = input("Enter type of vehicle (car/scooter): ").lower()
      if vehicle_type == "car" :
        seating_capacity = int(input("Enter number of seats: "))
        vehicle = ElectricCar(vehicle_id, model, battery_percentage, seating_capacity)

      elif vehicle_type == "scooter" :
        max_speed_limit = int(input("Enter maximum speed of the scooter: "))
        vehicle = ElectricScooter(vehicle_id, model, battery_percentage, max_speed_limit)
        
      else:
        print("Invalid input!. Enter valid input Scooter or Car")
        continue

      print()
      vehicle.maintainance_status = maintainance_status
      vehicle.rental_price = rental_price
      duplicate = [v for v in self.vehicles if v == vehicle]
      if duplicate:
        print(f"Duplicate vehicle ID '{vehicle.vehicle_id}' not allowed!")
        return
      self.vehicles.append(vehicle)
      self.fleet_hubs[hub_name].append(vehicle_id)



## Implementation of function calling and object creating
eco = EcoRideMain()
eco.greet()
while True:
  print()
  print("Choose an option you want to perform:\n1. Add Hub\n2. Add Vehicle\n3. Display Hubs\n4. Display Vehicles\n8. Exit")
  choice = int(input())
  match choice:
    case 1:
      eco.add_hub()
    case 2:
      eco.add_vehicles()
    case 3:
      for hub in eco.fleet_hubs.items():
        print(hub)
    case 4:
      for vehicle in eco.vehicles:
        print(vehicle.__dict__)
        print() 
    case 8: break
    case _: 
      print("Invalid choice!")
      break
