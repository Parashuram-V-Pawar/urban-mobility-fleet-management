from eco_ride_main import EcoRideMain

def greet():
    '''
    Displays a welcome message for the EcoRide Urban Mobility System.

    Returns: None
    '''
    print("\nWelcome to Eco-Ride Urban Mobility System")
    
def main():
    erm = EcoRideMain()
    erm.load_from_csv("data/fleet_data.csv")
    erm.load_from_json("data/fleet_data.json")
    erm.main()
    erm.save_to_csv("data/fleet_data.csv")
    erm.save_to_json("data/fleet_data.json")

if __name__ == "__main__":
  greet()
  main()
