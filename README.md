#  Travel Planner

A friendly, console-based travel planning app built with Python that helps you organize your next adventure!

> **Note:** This project was created following the VITyarthi - Build Your Own Project guidelines.

---

##  What is Travel Planner?

Travel Planner is a beginner-friendly command-line application that makes trip planning simple and fun. Choose your dream destination, set your dates and budget, add activities you're excited about, and instantly see your personalized itinerary come to life.

Perfect for Python beginners looking to build something practical and useful!

---

##  Features

- **Choose Your Destination** : Pick from Paris, New York, Tokyo, or Dubai
- **Set Your Dates** :Enter your travel start and end dates
- **Budget Tracking** :Keep track of your travel budget in USD
- **Activity Planning** :Add as many activities as you like (just type `done` when finished)
- **Smart Suggestions** :Get popular activity recommendations for your chosen destination
- **View Your Itinerary** :See everything organized in a clean, easy-to-read format

---

##  Technologies Used

- **Python 3.8+** (no external libraries needed!)
- Built entirely with Python's standard library

---

##  Getting Started

### Prerequisites

Make sure you have Python 3.8 or newer installed on your computer.

### Installation

1. **Download the script** – Save it as `travel_planner.py`

2. **(Optional) Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate     # On Linux/macOS
   venv\Scripts\activate        # On Windows
   ```

### Running the App

Simply run this command in your terminal:

```bash
python travel_planner.py
```

Or if you have both Python 2 and 3 installed:

```bash
python3 travel_planner.py
```

---

##  How to Use

When you launch the app, you'll see a simple menu:

```
--- Travel Planner Menu ---
1. Plan a new Trip
2. View Itinerary
3. Exit

Select an option (1-3):
```

### Example Session

Here's what planning a trip to Paris looks like:

```
Select an option (1-3): 1

Plan a new trip!
Enter your destination (Paris, New York, Tokyo, Dubai): Paris
Enter your start date (YYYY-MM-DD): 2025-12-01
Enter your end date (YYYY-MM-DD): 2025-12-07
Enter your travel budget in USD: 1500

What activities are you interested in? (Type 'done' when finished)
Activity: museum
Activity: cafe
Activity: done

Popular activities in Paris:
- Eiffel Tower, Louvre Museum
- Seine River

--- Your Travel Itinerary ---
Destination: Paris
Travel Dates: 2025-12-01 to 2025-12-07
Budget: $1500.00

Your chosen activities:
- Museum
- Cafe
---------------------------
```

---

##  Project Structure

```
travel-planner/
├── README.md
├── statement.md
├── travel_planner.py
├── tests/
│   └── test_travel_planner.py   # Optional unit tests
└── assets/
    └── screenshots/             # Optional screenshots
```

---

##  Testing

**Manual Testing:** Try different inputs and edge cases like invalid destinations, non-numeric budgets, or incorrect date formats to see how the app handles them.

**Unit Tests:** You can optionally add automated tests for validation logic in the `tests/` folder.

---

##  Known Issues & Room for Improvement

- **Date format validation** : Currently has some typos in prompts (like `YYYY-MM--DD`). Consider using Python's `datetime.strptime()` for better validation.
- **Spelling fixes** : A few destination suggestions have minor typos (e.g., "Eiffle Tower" should be "Eiffel Tower").
- **Better formatting** : The output could use more polish with improved spacing and visual design.
- **Save your plans** :Add the ability to save itineraries to a JSON file and load them later.
- **More destinations** :Expand the list beyond the current four cities.
- **Enhanced validation** – Add more robust input checking and error handling.

---

##  Future Enhancement Ideas

Want to take this project further? Here are some exciting possibilities:

- **Build a GUI** using Tkinter or create a web version with Flask
- **Integrate APIs** for real-time flight and hotel suggestions
- **Budget breakdown** with cost tracking for different categories
- **Calendar export** to iCal format for easy scheduling
- **Multiple itineraries** with full create, read, update, and delete functionality
- **Weather forecasts** for your destination dates
- **Collaborative planning** to share trips with friends

---

##  License

This is an educational project. Feel free to use, modify, and learn from it!

---

##  Acknowledgments

Built as part of the VITyarthi project initiative️.

