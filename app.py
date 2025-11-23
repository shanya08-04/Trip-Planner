from flask import Flask, render_template, request

class TravelPlanner:
    def __init__(self):
        self.available_destinations = {
            'Paris': ['Eiffle Tower , Louvre Museum', 'Seine River'],
            'New York': ['Statue of Liberty', 'Time Square', 'Central Park'],
            'Tokyo': ['Shibuya Crossing', 'Tokyo Tower', 'Meiji Shrine'],
            'Dubai': ['Burj Khalifa', 'Desert Safari', 'Palm jumeirah']
        }

    def get_popular_activities(self, destination):
        return self.available_destinations.get(destination, [])

app = Flask(__name__)
planner = TravelPlanner()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/plan', methods=['POST'])
def plan():
    destination = request.form.get('destination')
    start_date = request.form.get('start_date')
    end_date = request.form.get('end_date')
    budget = request.form.get('budget')
    activities = request.form.get('activities', '')
    activities_list = [a.strip() for a in activities.split(',') if a.strip()]
    error = None
    if destination not in planner.available_destinations:
        error = "Sorry, we don't have information for this destination."
    popular_activities = planner.get_popular_activities(destination)
    return render_template('itinerary.html',
        destination=destination,
        start_date=start_date,
        end_date=end_date,
        budget=budget,
        activities=activities_list,
        popular_activities=popular_activities,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)
