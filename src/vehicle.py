class Vehicle:

  def __init__(self, vehicle_id, model, battery_percentage):
    self.vehicle_id = vehicle_id
    self.model = model
    self.battery_percentage = battery_percentage

vehicle_id = "MEXB24CW2NT013567"
model = "XUV 700"
battery_percentage = 79
veh = Vehicle(vehicle_id,model,battery_percentage)
