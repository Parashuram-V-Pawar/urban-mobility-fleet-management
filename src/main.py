import csv
import json
from electric_car import ElectricCar
from electric_scooter import ElectricScooter

# Main controller class
class EcoRideMain:
  '''
    Main controller class for the EcoRide Urban Mobility System.

    This class manages fleet hubs and electric vehicles, it gives menu-driven operations such as adding hubs, managing vehicles, displaying fleet information, and handling data persistence.

    Attributes:
        fleet_hubs (dict): Stores hub names as keys and lists of vehicles assigned to each hub as values.
        vehicles (list): Stores all vehicle objects managed by the system.
  '''
  # Empty dictionary to store hubs and vehicles
  fleet_hubs = dict()
  # Empty list to store the vehicle details
  vehicles = []
  # Function desplays a welcome message
  def greet(self):
    '''
    Displays a welcome message for the EcoRide Urban Mobility System.

    Returns: None
    '''
    print("\nWelcome to Eco-Ride Urban Mobility System")

  def main(self):
    '''
    Acts as the main control loop for the EcoRide Urban Mobility System.

    This method continuously displays the menu, accepts user input, and routes the control flow to the appropriate hub and vehicle management functions until the user exits the application.

    Returns: None
    '''
    while True:
      print()
      print("Choose an option you want to perform:\n1. Add Hub\n2. Add Vehicle\n3. Display Hubs\n4. Display Vehicles\n5. Search by battery\n6. View vehicles\n7. Vehicle maintainance status\n8. Sort vehicles\n9. Sort by\n10. Exit")
      choice = int(input())
      match choice:
        case 1:
          eco.add_hub()
        case 2:
          eco.add_vehicles()
        case 3:
          for hub, vehicle_list in eco.fleet_hubs.items():
            print(f"{hub} : {vehicle_list}")
        case 4:
          for vehicle in eco.vehicles:
            print(vehicle)
            print() 
        case 5:
          veh_battery = list(filter(lambda vehicle: vehicle.battery_percentage > 80 , eco.vehicles))
          for v in veh_battery:
            print(f"{v.vehicle_id} | {v.model} | {v.battery_percentage}")
        case 6:
          eco.view_vehicle_by_vehicle_type()
        case 7:
          eco.vehicle_maintainance_status()
        case 8:
          hub_name = input("Enter hub name to sort vehicles: ")
          eco.vehicle_sorting(hub_name)
        case 9: 
          sort_by = input("Sort by (battery/rental price):")
          eco.advanced_sorting(sort_by)
        case 10: break
        case _: 
          print("Invalid choice!")
          break




  # Function to add hub.
  def add_hub(self):
    '''
    Function to add hub to the fleet_hubs

    This method prompts user to add hub name, if the hub already exist in the fleet_hubs, a message is displayed else, the hub will be added to the fleet with empty list
    
    Returns: None
    '''
    hub_name = input("Enter hub name: ")
    if hub_name in self.fleet_hubs:
      print(f"Hub {hub_name} already present.")
    else:
      self.fleet_hubs[hub_name] = []
      print(f"{hub_name} was added successfully.")
    
    print(self.fleet_hubs)



  # Function to take vehicles inputs.
  def add_vehicles(self):
    '''
    Function to add vehicles

    This method allows the user to enter multiple vehicle details (such as vehicle ID, model, and type) and assigns them to an existing hub in the fleet.

    Returns: None
    
    '''
    hub_name = input("Enter hub name to add vehicles: ")
    if hub_name not in self.fleet_hubs:
      print(f"Hub {hub_name} is not present. Please add Hub first")
      return
    
    no_of_vehicles = int(input("Enter number of vehicles to add: \n"))
    for i in range(no_of_vehicles):
      print(f"Enter details for {i+1} vehicle")
      vehicle_type = input("Enter type of vehicle (car/scooter): ").lower()
      if vehicle_type.lower() != "car" and vehicle_type.lower() != "scooter":
        print("\nVehicle type must be car or scooter.")
        return
      vehicle_id = input("Enter vehicle id: ")
      model = input("Enter vehicle model: ")
      battery_percentage = int(input("Enter available battery percentage: "))
      maintainance_status = input("Enter maintainance status(Available/ On Trip/ Under Maintainance): ")
      rental_price = int(input("Enter Rental price of the vehicle: "))

      if vehicle_type == "car" :
        seating_capacity = int(input("Enter number of seats: "))
        vehicle = ElectricCar(vehicle_id, model, battery_percentage, seating_capacity)

      elif vehicle_type == "scooter" :
        max_speed_limit = int(input("Enter maximum speed of the scooter: "))
        vehicle = ElectricScooter(vehicle_id, model, battery_percentage, max_speed_limit)
       
      print()
      vehicle.maintainance_status = maintainance_status
      vehicle.rental_price = rental_price
      duplicate = [v for v in self.vehicles if v == vehicle]
      if duplicate:
        print(f"Duplicate vehicle ID '{vehicle.vehicle_id}' not allowed!")
        return
      self.vehicles.append(vehicle)
      self.fleet_hubs[hub_name].append(vehicle_id)


  # Function to display vehicle by its type.
  def view_vehicle_by_vehicle_type(self):
    '''
    Method to display vehicle grouped by its vehicle type

    THis method displays all vehicles with group of that type across all hubs in the fleet.

    Returns: None
    
    '''
    self.vehicle_category = {
      "Cars":[],
      "Scooters":[]
    }

    for vehicle in self.vehicles:
      if isinstance(vehicle, ElectricCar):
        self.vehicle_category["Cars"].append(vehicle)
      elif isinstance(vehicle, ElectricScooter):
        self.vehicle_category["Scooters"].append(vehicle)
    
    for vehicle_type, vehicle_list in self.vehicle_category.items():
      print(f"\n{vehicle_type} : ")
      print("--------------------------")
      if not vehicle_list:
        print("No vehicles in list")
      for v in vehicle_list:
        print(f"{v}")


  # Function to display vehicle maintainance status
  def vehicle_maintainance_status(self):
    '''
    Function to count vehicles in reference to maintainance status.

    This method counts the vehicles based on its maintainance status and displays status wise numbers

    Returns: None

    '''
    available = 0
    on_trip = 0
    under_maintainance = 0
    for vehicle in self.vehicles:
      status = vehicle.maintainance_status.lower()

      if status == "available":
        available += 1
      elif status == "on trip":
        on_trip += 1
      elif status == "under maintainance":
        under_maintainance += 1

    print("\n\nMaintainance Status: ")
    print("------------------------------------------------")
    print(f"Available: {available}")
    print(f"On trip: {on_trip}")
    print(f"Under Maintainance: {under_maintainance}")


  # Function to sort vehicle by name
  def vehicle_sorting(self, hub_name: str):
    '''
    Function to sort vehicle results based on the model number in specified hub.
    
    :param hub_name: Hub name from which we need to sort the results based on the model number.

    '''
    if hub_name not in self.fleet_hubs:
      return
    hub_vehicles = [
      v for v in self.vehicles if v.vehicle_id in self.fleet_hubs[hub_name]
    ]
    hub_vehicles.sort(key=lambda v: v.model.lower())
    if not hub_vehicles:
      print("No vehicles in hub.")
      return
    print(f"\n\nVehicles in '{hub_name}' (sorted by model):")
    print("-------------------------------------------------")
    for vehicle in hub_vehicles:
        print(f"\n{vehicle}")

  # Sorting dynamically by battery or rental_price
  def advanced_sorting(self, sort_by: str):
    '''
    Function to sort the result based on the user input
    
    :param sort_by: Input received from the user based on what the sorting is to be performed
    '''
    if sort_by.lower() == "battery":
        sorted_vehicles = sorted(
            self.vehicles,
            key=lambda v: v.battery_percentage,
            reverse=True
        )
    elif sort_by.lower() == "rental price":
        sorted_vehicles = sorted(
            self.vehicles,
            key=lambda v: v.rental_price,
            reverse=True
        )
    else:
        print("Invalid sorting option.")
        return
    print(f"\n\nVehicles sorted by {sort_by}:")
    for v in sorted_vehicles:
        print(f"\n{v}")

  # Function to write to csv
  def save_to_csv(self, filename: str):
    '''
    Function to save the data to the CSV file
    
    :param filename: filename where the data is to be saved for later use

    '''
    import csv
    with open(filename, mode="w", newline="") as file:
      writer = csv.writer(file)
      writer.writerow(["hub_name","vehicle_id","model","battery_percentage","maintainance_status","rental_price","vehicle_type","extra"])

      for hub, vehicle_ids in self.fleet_hubs.items():
        for vid in vehicle_ids:
          vehicle = next(v for v in self.vehicles if v.vehicle_id == vid)
          if vehicle.__class__.__name__ == "ElectricCar":
            vehicle_type = "Car"
            extra = vehicle.seating_capacity
          else:
            vehicle_type = "Scooter"
            extra = vehicle.max_speed_limit
          writer.writerow([hub, vehicle.vehicle_id, vehicle.model, vehicle.battery_percentage,vehicle.maintainance_status, vehicle.rental_price, vehicle_type, extra])
    print(f"Fleet data saved to CSV successfully.")


  # Function to load data from CSV file
  def load_from_csv(self, filename: str):
    '''
    Function to load data from the CSV file
    
    :param filename: filename from where the data is to be loaded.

    '''
    try:
      with open(filename, mode="r", newline='') as file:
        reader = csv.DictReader(file)
        self.vehicles.clear()
        self.fleet_hubs.clear()

        for row in reader:
          hub_name = row["hub_name"]
          vehicle_id = row["vehicle_id"]
          model = row["model"]
          battery = int(row["battery_percentage"])
          status = row["maintainance_status"]  
          price = int(row["rental_price"])
          vehicle_type = row["vehicle_type"].lower()
          extra = int(row["extra"])

          if vehicle_type == "car":
            vehicle = ElectricCar(vehicle_id, model, battery, extra)
          elif vehicle_type == "scooter":
            vehicle = ElectricScooter(vehicle_id, model, battery, extra)
          else:
            print(f"Unknown vehicle type '{vehicle_type}' in CSV. Skipping...")
            continue

          vehicle.maintainance_status = status
          vehicle.rental_price = price

          self.vehicles.append(vehicle)

          # Add vehicle ID to hub dictionary
          if hub_name not in self.fleet_hubs:
            self.fleet_hubs[hub_name] = []
          self.fleet_hubs[hub_name].append(vehicle_id)
      print("Fleet data loaded from CSV successfully.")

    except FileNotFoundError:
      print("CSV file not found. Starting with empty fleet.")
    except KeyError as e:
      print(f"Missing expected column in CSV: {e}")
    except Exception as e:
      print(f"Error loading CSV: {e}")

  # Function to load data from JSON
  def load_from_json(self, filename: str):
    '''
    This function loads information from the json file to the program
    
    :param filename: filename from where the data is to be loaded

    '''
    try:
      with open(filename, "r") as f:
        fleet_data = json.load(f)
      
      self.vehicles.clear()
      self.fleet_hubs.clear()

      for hub_name, vehicle_list in fleet_data.items():
        self.fleet_hubs[hub_name] = []
        for vdata in vehicle_list:
          vehicle_type = vdata["vehicle_type"].lower()
          extra = vdata["extra"]
          if vehicle_type == "electriccar":
            vehicle = ElectricCar(vdata["vehicle_id"], vdata["model"], vdata["battery_percentage"], extra)
          elif vehicle_type == "electricscooter":
            vehicle = ElectricScooter(vdata["vehicle_id"], vdata["model"], vdata["battery_percentage"], extra)
          else:
            print(f"Unknown vehicle type '{vehicle_type}' in JSON. Skipping...")
            continue

          vehicle.maintainance_status = vdata["maintainance_status"]
          vehicle.rental_price = vdata["rental_price"]

          self.vehicles.append(vehicle)
          self.fleet_hubs[hub_name].append(vehicle.vehicle_id)
      
      print(f"Fleet data loaded from {filename} successfully.")

    except FileNotFoundError:
      print(f"{filename} not found. Starting with empty fleet.")
    except Exception as e:
      print(f"Error loading JSON: {e}")


  # Function to save data to JSON
  def save_to_json(self, filename: str):
    '''
    Function to store hub and vehicle information to JSON
    
    :param filename: takes filename as input where the data needs to be saved

    '''
    fleet_data = {}
    for hub, vehicle_ids in self.fleet_hubs.items():
      fleet_data[hub] = []
      for vid in vehicle_ids:
        vehicle = next(v for v in self.vehicles if v.vehicle_id == vid)
        fleet_data[hub].append(self.vehicle_to_dict(vehicle))
    
    with open(filename, "w") as f:
      json.dump(fleet_data, f, indent=4)
    print(f"Fleet data saved to {filename} successfully.")

  # Function to convert vehicle data to dictionary
  def vehicle_to_dict(self, vehicle):
    '''
    Function to convert vehicle information to dictionary to save in JSON
    
    :param vehicle: It is a single vehicle object to be converted into dict
    '''
    data = {
      "vehicle_id": vehicle.vehicle_id,
      "model": vehicle.model,
      "battery_percentage": vehicle.battery_percentage,
      "maintainance_status": vehicle.maintainance_status,  
      "rental_price": vehicle.rental_price,
      "vehicle_type": vehicle.__class__.__name__,  
    }

    if isinstance(vehicle, ElectricCar):
      data["extra"] = vehicle.seating_capacity
    else:
      data["extra"] = vehicle.max_speed_limit
    return data




## Implementation of function calling and object creating
eco = EcoRideMain()
eco.greet()

if __name__ == "__main__":
  eco.load_from_csv("data/fleet_data.csv")
  eco.load_from_json("data/fleet_data.json")
  eco.main()
  eco.save_to_csv("data/fleet_data.csv")
  eco.save_to_json("data/fleet_data.json")