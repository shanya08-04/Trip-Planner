

class TravelPlanner:
    def __init__(self):
        self.destinations = None
        self.start_date = None
        self.end_date = None
        self.budget = None
        self.activities = []
        self.available_destinations ={ 
            'Paris':['Eiffle Tower , Louvre Museum', 'Seine River'],
            'New York':['Statue of Liberty','Time Square','Central Park'],
            'Tokyo':['Shibuya Crossing','Tokyo Tower', 'Meiji Shrine'],
            'Dubai':['Burj Khalifa','Desert Safari','Palm jumeirah']
        }
    def get_user_input(self):
        print("Plan a new trip!")
        self.destinations = input("Enter your destination (Paris,New York, Tokyo, Dubai):").title()
        if self.destinations not in self.available_destinations:
            print("Sorry , we don't have information for this destination.")
            return
        self.start_date = input("Enter your start date(YYYY-MM--DD):")
        self.end_date = input("Enter your end date(YYY-MM-DD):")
        self.budget = float(input("Enter your travel budget in USD:"))
        print("What activities are you interested in?(Type 'done' when finished)")
        self.activities = []  #clear previous activities
        while True:
            activity =input("Activity:").capitalize()
            if activity == 'Done':
                break
            self.activities.append(activity)
    def suggest_activities(self):
        if self.destinations in self.available_destinations:
            print(f"\nPopular activites in {self.destinations}:")
            for activity in self.available_destinations[self.destinations]:
                print(f"- {activity}")
    def display_itinerary(self):
        if not self.destinations:
            print("\nNo trip planned yet. Please a new trip first!")
            return
        print("\n---Your Travel Itinerary---")
        print(f"Destinations:{self.destinations}")
        print(f"Travel Dates:{self.start_date}to{self.end_date}")
        print(f"Budget:${self.budget:2f}")
        print("Your chosen activities:")
        for activity in self.activities:
            print(f"-{activity}")
        print("---------------------------")
    def show_menu(self):
        while True:
            print("\n---Travel Planner Menu---")
            print("1.Plan a new Trip")
            print("2.View Itinerary")
            print("3. Exit")
            choice = input("select an option (1-3):")
            if choice == "1":
                self.get_user_input()
                self.suggest_activities()
            elif choice == "2":
                self.display_itinerary()
            elif choice =="3":
                print("Thank you for using the Travel Planner! Goodbye!")
                break
            else:
                print("Invalid option . Please choose 1,2,or 3.")
if __name__ == "__main__":
    planner = TravelPlanner()
    planner.show_menu()

    