from electric_car import ElectricCar
from electric_scooter import ElectricScooter

class EcoRideMain:
  vehicles = []
  def greet(self):
    print("Welcome to Eco-Ride Urban Mobility System")

  def eco_ride_functioning(self):
    no_of_vehicles = int(input("Enter number of vehicles to add: \n"))

    # self.vehicles = []
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
      self.vehicles.append(vehicle)


eco = EcoRideMain()
eco.greet()
eco.eco_ride_functioning()

for vehicle in eco.vehicles:
  print(vehicle.__dict__)
  print()

