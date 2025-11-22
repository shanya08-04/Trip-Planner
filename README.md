# Travel Planner

A simple console-based Travel Planner written in Python.  
This small project lets a user plan a basic trip by choosing a destination, travel dates, budget and activities, then view the generated itinerary.

**Project guidelines used:** VITyarthi - Build Your Own Project (see uploaded guideline PDF). :contentReference[oaicite:0]{index=0}  
You can also open the guideline file in this workspace: `/mnt/data/vithyarthi project.pdf`

---

## Project title
**Travel Planner**

## Overview
`Travel Planner` is a beginner-friendly CLI application that helps users create a basic travel itinerary by selecting a destination from a small built-in list, entering travel dates and budget, and adding desired activities. The app also suggests popular activities for the chosen destination.

## Features
- Choose from available destinations (Paris, New York, Tokyo, Dubai)
- Enter travel start/end dates and budget
- Add multiple activities (type `done` to finish)
- View a formatted itinerary
- Simple menu-driven CLI interface

## Technologies / Tools used
- Python 3.8+ (recommended)
- Plain Python standard library — no external dependencies

## Installation
1. Ensure you have Python 3.8 or newer installed.
2. Save the provided script as `travel_planner.py` (or any filename you prefer).
3. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate     # Linux / macOS
   venv\Scripts\activate        # Windows
How to run
From the command line:

bash
Copy code
python travel_planner.py
Or, if you have both Python2 and Python3:

bash
Copy code
python3 travel_planner.py
Example Session
sql
Copy code
---Travel Planner Menu---
1.Plan a new Trip
2.View Itinerary
3. Exit
select an option (1-3): 1
Plan a new trip!
Enter your destination (Paris,NewYork, Tokyo, Dubai): Paris
Enter your start date(YYYY-MM--DD): 2025-12-01
Enter your end date(YYY-MM-DD): 2025-12-07
Enter your travel budget in USD: 1500
What activities are you interested in?(Type 'done' when finished)
Activity: museum
Activity:cafe
Activity:done

Popular activites in Paris:
- Eiffel Tower , Louvre Museum
- Seine River

---Your Travel Itinerary---
Destinations: Paris
Travel Dates: 2025-12-01 to 2025-12-07
Budget: $1500.000000
Your chosen activities:
- Museum
- Cafe
---------------------------
Project structure (suggested)
bash
Copy code
travel-planner/
├── README.md
├── statement.md
├── travel_planner.py
├── tests/
│   └── test_travel_planner.py   # optional unit tests
└── assets/
    └── screenshots/             # optional screenshots for README
Testing / Validation
Manual testing via the CLI: test each menu item and input edge cases (invalid destination, non-numeric budget, date formats).

(Optional) Add unit tests for validation logic (e.g., checking destination lookup, budget parsing).

Known issues & suggested improvements
Input date format in the code contains typos (YYYY-MM--DD, YYY-MM-DD). Consider validating dates with datetime.strptime() and prompting again on invalid input.

Destination suggestions have small typos (e.g., Eiffle Tower → Eiffel Tower, Time Square → Times Square, Palm jumeirah → Palm Jumeirah). Fix spelling in available_destinations.

Improve user experience with better formatting and spacing.

Add persistent storage (save itineraries to a JSON file) and ability to load previous plans.

Add more destinations and richer activity lists.

Add unit tests and input validation modules.

Future enhancements (project extension ideas)
GUI (Tkinter / web-based Flask app) to make it interactive.

Integrate a public API for real-time flight/hotel suggestions.

Add cost breakdown & simple budget planner.

Add calendar integration or export to iCal format.

Save multiple itineraries with CRUD operations.
