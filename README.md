# urban-mobility-fleet-management

It is a system to manage fleets, vehicles and monitor vehicle maintainance status in real-time.

## Features:
1. Adding Fleet hubs.
2. Adding vehicle details to hub.
3. Viewing vehicles with their types.
4. Monitor vehicle maintainance status.
5. Sorting vehicles based on it's hub.
6. Sorting vehicles by battery percentage/ Rental price.
7. Save information to CSV and JSON files.
8. Retrieving information from CSV and JSON files.

## Tech stack
```
-- Language: Python
-- Tools: VSCode, Git
-- Testing: Pytest
```

## Project structure
```
Urban-mobility-fleet-management
|-- src
|   |-- main.py
|   |-- eco_ride_main.py
|   |-- vehicle.py
|   |-- electric_car.py
|   |-- electric_scooter.py
|
|-- test
|   |-- test_eco_ride_main.py
|   |-- test_electric_car.py
|   |-- test_electric_scooter.py
|
|-- data
|   |-- fleet_data.csv
|   |-- fleet_data.json
|
|-- .gitignore
|-- README.md
|-- requirements.txt
```

## Installation

Clone the repository
-> git clone https://github.com/Parashuram-V-Pawar/urban-mobility-fleet-management.git

Move to project folder
-> cd urban-fleet-management

Install dependencies
-> pip install -r requirements.txt

Run the application
-> python main.py


## Author
```
Parashuram V Pawar
GitHub username: Parashuram-V-Pawar
```