from vehicle import Vehicle

class ElectricCar(Vehicle):
  
  def __init__(self, vehicle_id, model, battery_percentage, seating_capacity):
    super().__init__(vehicle_id, model, battery_percentage)
    self.seating_capacity = seating_capacity

  @property
  def battery_percentage(self):
    return self.__battery_percentage
  
  @battery_percentage.setter
  def battery_percentage(self, batter_percentage):
    self.__battery_percentage = batter_percentage

car = ElectricCar("MDC09876XD","XUV 3X0",102,5)
# car.maintainance_status = "Service done"
# car.rental_price = 80
# print(car.__dict__)

print(car.__dict__)