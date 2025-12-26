from vehicle import Vehicle

class ElectricScooter(Vehicle):
  
  def __init__(self, vehicle_id: str, model: str, battery_percentage: int,  max_speed_limit: int):
    super().__init__(vehicle_id, model, battery_percentage)
    self. max_speed_limit =  max_speed_limit

  def calculate_trip_cost(self, distance):
    # $1.00 base + $0.15 per minute
    return 1 + (0.15 * distance)
  
  def __str__(self):
    return (f"{super().__str__()}\nMaximum Speed Limit: {self.max_speed_limit}\n")