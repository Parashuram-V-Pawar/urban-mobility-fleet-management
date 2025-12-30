import pytest
from eco_ride_main import EcoRideMain
from electric_car import ElectricCar
from electric_scooter import ElectricScooter
  
@pytest.fixture
def fleet_data():
  fleet_hub = {}
  car1 = ElectricCar("1243", "Innova", 78, 7)
  car1.maintainance_status = "Available"
  car1.rental_price = 750

  car2 = ElectricCar("1244", "Innova", 85, 7)
  car2.maintainance_status = "On Trip"
  car2.rental_price = 770

  car3 = ElectricCar("1245", "Creta", 88, 5)
  car3.maintainance_status = "under maintainance"
  car3.rental_price = 550

  scooter1 = ElectricScooter("2345", "Activa", 98, 110)
  scooter1.maintainance_status = "under maintainance"
  scooter1.rental_price = 250

  scooter2 = ElectricScooter("2346", "Access", 65, 100)
  scooter2.maintainance_status = "On Trip"
  scooter2.rental_price = 180

  scooter3 = ElectricScooter("2347", "Dio", 76, 90)
  scooter3.maintainance_status = "Available"
  scooter3.rental_price = 150

  vehicles = [car1, car2, car3, scooter1, scooter2, scooter3]

  fleet_hub["Airport"] = ["1243", "2345", "1245", "2346"]
  fleet_hub["DownTown"] = ["1244", "2347"]

  return fleet_hub, vehicles

def test_add_vehicle(monkeypatch):
  eco = EcoRideMain()

  eco.fleet_hubs["Airport"] = []

  inputs = iter(["Airport",
                 "2",
                 "car",
                 "2321",
                 "Cyberster",
                 98,
                 "Available",
                 2000,
                 4,
                 "scooter",
                 "2322",
                 "Activa 6g",
                 78,
                 "On Trip",
                 340,
                 110])
  monkeypatch.setattr("builtins.input",lambda _: next(inputs))

  eco.add_vehicles()

  assert len(eco.vehicles) == 2
  assert isinstance(eco.vehicles[0], ElectricCar)
  assert eco.vehicles[0].vehicle_id == "2321"
  assert eco.vehicles[0].model == "Cyberster"
  assert eco.vehicles[0].battery_percentage == 98
  assert eco.vehicles[0].maintainance_status == "Available"
  assert eco.vehicles[0].rental_price == 2000
  assert eco.vehicles[0].seating_capacity == 4

  assert isinstance(eco.vehicles[1], ElectricScooter)
  assert eco.vehicles[1].vehicle_id == "2322"
  assert eco.vehicles[1].model == "Activa 6g"
  assert eco.vehicles[1].battery_percentage == 78
  assert eco.vehicles[1].maintainance_status == "On Trip"
  assert eco.vehicles[1].rental_price == 340
  assert eco.vehicles[1].max_speed_limit == 110


# Invalid inouts
  with pytest.raises(ValueError, match="Vehicle type must be car or scooter"):
    inputs = iter([
        "Airport",
        1,
        "bike",
        "999",
        "Test",
        50,
        "Available",
        100,
        2
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    eco.add_vehicles()
    
def test_view_vehicle_by_vehicle_type(fleet_data):

  fleet_hubs, vehicles = fleet_data

  eco = EcoRideMain()

  eco.vehicles = vehicles

  eco.view_vehicle_by_vehicle_type()

  assert len(eco.vehicle_category["Cars"]) == 3
  assert len(eco.vehicle_category["Scooters"]) == 3

def test_vehicle_maintainance_status(capsys, fleet_data):
  fleet_hubs, vehicles = fleet_data

  eco = EcoRideMain()

  eco.vehicles = vehicles
  eco.vehicle_maintainance_status()

  output = capsys.readouterr()

  assert str("\n\nMaintainance Status: \n------------------------------------------------\nAvailable: 2\nOn trip: 2\nUnder Maintainance: 2\n") in output
  
def test_vehicle_sorting(capsys, fleet_data):
    fleet_hubs, vehicles = fleet_data
    
    eco = EcoRideMain()

    eco.vehicles = vehicles

    eco.fleet_hubs = fleet_hubs

    eco.vehicle_sorting("Airport")

    captured = capsys.readouterr()

    assert "Vehicles in 'Airport' (sorted by model):" in captured.out
    assert "Activa" in captured.out
    assert "Innova" in captured.out
    assert "Creta" in captured.out

    eco.vehicle_sorting("DownTown")

    captured = capsys.readouterr()

    assert "Vehicles in 'DownTown' (sorted by model):" in captured.out
    assert "Dio" in captured.out
    assert "Innova" in captured.out

def test_advanced_sorting_by_battery(capsys, fleet_data):
    fleet_hubs, vehicles = fleet_data
    eco = EcoRideMain()
    
    eco.vehicles = vehicles

    eco.advanced_sorting("battery")

    captured = capsys.readouterr()

    assert "\n\nVehicles sorted by battery:\n\nActiva\n\nCreta\n\nInnova\n\nInnova\n\nDio\n\nAccess\n" in captured

def test_save_to_csv(capsys, fleet_data):

  fleet_hubs, vehicles = fleet_data
  eco = EcoRideMain()
  eco.fleet_hubs = fleet_hubs
  eco.vehicles = vehicles

  eco.save_to_csv("test_file.csv")
  output = capsys.readouterr()

  assert "Fleet data saved to CSV successfully.\n" in output

def test_save_to_json(capsys, fleet_data):
  fleet_hubs, vehicles = fleet_data
  eco = EcoRideMain()
  eco.fleet_hubs = fleet_hubs
  eco.vehicles = vehicles

  eco.save_to_json("test_file.json")
  output = capsys.readouterr()

  assert "Fleet data saved to JSON successfully.\n" in output

def test_load_from_csv(capsys):
  eco = EcoRideMain()

  eco.load_from_csv("test_file.csv")
  output = capsys.readouterr()

  assert "Fleet data loaded from CSV successfully.\n" in output

def test_vehicle_to_dict(fleet_data):
  fleet_hubs, vehicles = fleet_data
  eco = EcoRideMain()
  eco.vehicles = vehicles

  vehicle_dicts = [eco.vehicle_to_dict(vehicle) for vehicle in eco.vehicles]

  assert vehicle_dicts[0] == {
    "vehicle_id": "1243",
    "model": "Innova",
    "battery_percentage": 78,
    "maintainance_status": "Available",
    "rental_price": 750,
    "extra": 7,
    'vehicle_type': 'ElectricCar'
  }

  assert vehicle_dicts[3] == {
    "vehicle_id": "2345",
    "model": "Activa",
    "battery_percentage": 98,
    "maintainance_status": "under maintainance",
    "rental_price": 250,
    "extra": 110,
    'vehicle_type': 'ElectricScooter'
  }
  