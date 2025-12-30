import pytest
from electric_car import ElectricCar

@pytest.fixture
def set_car():
  car1 = ElectricCar("1243", "Innova", 78, 7)
  car1.maintainance_status = "Available"
  car1.rental_price = 750
  car2 = ElectricCar("1244", "Innova", 85, 7)
  car2.maintainance_status = "On Trip"
  car2.rental_price = 770
  car3 = ElectricCar("1245", "Creta", 88, 5)
  car3.maintainance_status = "under maintainance"
  car3.rental_price = 550
  vehicles = [car1, car2, car3]
  return vehicles

@pytest.mark.parametrize("distance, expected_cost", [
    (20, 15),
    (30, 20),
    (250, 130)
])
def test_calculate_trip_cost(set_car, distance, expected_cost):
    car = set_car[0]
    assert car.calculate_trip_cost(distance) == expected_cost

def test_str_method(set_car):
    car = set_car[0]
    expected_str = ("Vehicle Id: 1243\nModel: Innova\nBattery Percentage: 78\n"
                    "Maintainance Status: Available\nRental Price: 750\n"
                    "Seating Capacity: 7\n")
    print(car)
    assert str(car) == expected_str
    
def test_electric_car_equality(set_car):
    car1 = set_car[0]
    car2 = ElectricCar("1243", "Innova", 90, 7)  
    car3 = set_car[1]

    assert car1 == car2
    assert car1 != car3 