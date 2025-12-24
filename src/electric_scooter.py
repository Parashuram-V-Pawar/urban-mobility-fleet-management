from vehicle import Vehicle

class ElectricScooter(Vehicle):
  
  def __init__(self, vehicle_id, model, battery_percentage,  max_speed_limit):
    super().__init__(vehicle_id, model, battery_percentage)
    self. max_speed_limit =  max_speed_limit

scooter = ElectricScooter("SCO9876WE23","Simple One",67,120)
# scooter.maintainance_status = "Service done"
# scooter.rental_price = 80

print(scooter.__dict__)