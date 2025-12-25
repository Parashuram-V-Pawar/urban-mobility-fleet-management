from vehicle import Vehicle

class ElectricCar(Vehicle):
  
  def __init__(self, vehicle_id, model, battery_percentage, seating_capacity):
    super().__init__(vehicle_id, model, battery_percentage)
    self.seating_capacity = seating_capacity

  def calculate_trip_cost(self, distance):
    # $5.00 base + $0.50 per km
    return 5.00 + (0.5 * distance)

# car = ElectricCar("MDC09876XD","XUV 3X0",100,5)
# # car.maintainance_status = "Service done"
# # car.rental_price = 80

# print(car.__dict__)