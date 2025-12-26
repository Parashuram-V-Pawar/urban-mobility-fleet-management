from vehicle import Vehicle

class ElectricCar(Vehicle):
  
  def __init__(self, vehicle_id: str, model: str, battery_percentage: int, seating_capacity: int):
    super().__init__(vehicle_id, model, battery_percentage)
    self.seating_capacity = seating_capacity

  def calculate_trip_cost(self, distance):
    # $5.00 base + $0.50 per km
    return 5.00 + (0.5 * distance)
  
  def __str__(self):
    return (f"{super().__str__()}\nSeating Capacity: {self.seating_capacity}\n")