from vehicle import Vehicle

class ElectricScooter(Vehicle):
  
  def __init__(self, vehicle_id, model, battery_percentage,  max_speed_limit):
    super().__init__(vehicle_id, model, battery_percentage)
    self. max_speed_limit =  max_speed_limit

  def calculate_trip_cost(self, distance):
    # $1.00 base + $0.15 per minute
    return 1 + (0.15 * distance)
  
  def __str__(self):
    return (f"{super().__str__()}\nMaximum Speed Limit: {self.max_speed_limit}\n")

# scooter = ElectricScooter("SCO9876WE23","Simple One",67,120)
# # scooter.maintainance_status = "Service done"
# # scooter.rental_price = 80

# print(scooter.__dict__)