import pytest
from electric_scooter import ElectricScooter

@pytest.fixture
def set_scooter():
  scooter1 = ElectricScooter("2345", "Activa", 98, 110)
  scooter1.maintainance_status = "under maintainance"
  scooter1.rental_price = 250

  scooter2 = ElectricScooter("2346", "Access", 65, 100)
  scooter2.maintainance_status = "On Trip"
  scooter2.rental_price = 180

  scooter3 = ElectricScooter("2347", "Dio", 76, 90)
  scooter3.maintainance_status = "Available"
  scooter3.rental_price = 150

  vehicles = [scooter1, scooter2, scooter3]

  return vehicles

@pytest.mark.parametrize("distance, expected_cost", [
    (20, 4),
    (30, 5.5),
    (250, 38.5)
])
def test_calculate_trip_cost(set_scooter, distance, expected_cost):
  scooter = set_scooter[0]
  assert scooter.calculate_trip_cost(distance) == expected_cost

def test_str_method(set_scooter):
  scooter = set_scooter[0]
  expected_str = ("Vehicle Id: 2345\nModel: Activa\nBattery Percentage: 98\n"
                  "Maintainance Status: under maintainance\nRental Price: 250\n"
                  "Maximum Speed Limit: 110\n")
  print(scooter)
  assert str(scooter) == expected_str

def test_electric_scooter_equality(set_scooter):
  scooter1 = set_scooter[0]
  scooter2 = ElectricScooter("2345","Activa",98, 110)
  scooter3 = set_scooter[2]
  scooter4 = set_scooter[1]

  assert scooter1 == scooter2
  assert scooter2 != scooter3
  assert scooter1 != scooter4