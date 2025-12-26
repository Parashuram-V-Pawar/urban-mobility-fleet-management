from abc import ABC, abstractmethod

class Vehicle(ABC):
  def __init__(self, vehicle_id, model, battery_percentage):
    self.vehicle_id = vehicle_id
    self.model = model
    self.battery_percentage = battery_percentage
    self.__maintainance_status = None
    self.__rental_price = None

  # getter and setter for battery_percentage
  @property
  def battery_percentage(self):
    return self.__battery_percentage
  
  @battery_percentage.setter
  def battery_percentage(self, battery_percentage):
    if battery_percentage >= 0 and battery_percentage <= 100:
      self.__battery_percentage = battery_percentage
    else:
      raise ValueError("Battery percentage should be within 0 and 100")
  
  
  # getter and setter for maintaince_status
  def get_maintainance_status(self):
    return self.__maintainance_status
  
  def set_maintainance_status(self, maintainance_status):
    self.__maintainance_status = maintainance_status
  
  # getter and setter for rental_price
  def set_rental_price(self, rental_price):
    if rental_price < 0:
      raise ValueError("Rental price cannot be negative")
    else:
      self.__rental_price = rental_price

  def get_rental_price(self):
    return self.__rental_price
  
  maintainance_status = property(get_maintainance_status, set_maintainance_status)
  rental_price = property(get_rental_price, set_rental_price)


  # Abstract method to calculate trip cost
  @abstractmethod 
  def calculate_trip_cost(self, distance):
    pass

  def __eq__(self,other):
    return self.vehicle_id == other.vehicle_id
  
  def __str__(self):
    return (f"Vehicle Id: {self.vehicle_id}\nModel: {self.model}\nBattery Percentage: {self.battery_percentage}\nMaintainance Status: {self.maintainance_status}\nRental Price: {self.rental_price}")


# initialize class object and assign values
# vehicle_id = "MEXB24CW2NT013567"
# model = "XUV 700"
# battery_percentage = 79
# veh = Vehicle(vehicle_id,model,battery_percentage)

# print(f"Model: {veh.model}")
# print(f"Vehicle ID: {veh.vehicle_id}")
# print(f"Battery Percentage: {veh.battery_percentage}")
# veh.maintainance_status = "Pending"
# print(f"Maintainance Status: {veh.maintainance_status}")

# veh.rental_price = 100
# print(f"Rental price: {veh.rental_price}")
