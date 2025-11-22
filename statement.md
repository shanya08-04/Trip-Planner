
# Statement of the Project : Travel Planner

## Problem statement
Many beginner travelers need a quick and simple tool to quickly draft a travel itinerary and keep track of dates, budget, and activities. The goal of this project is to provide a simple, easy-to-use console application that allows users to plan trips, view popular activities for a chosen destination, and review the itinerary.

## Scope of the project
This is a small-scale project intended for learning and demonstration purposes that covers:
- A console-based user interface for planning a single trip.
- A predefined set of destinations with suggested activities.
- Input and storage (in-memory) of travel dates, budget, and chosen activities.
- Displaying a formatted itinerary.
- No external API integrations or persistent storage in the initial version.

Planned scope (can be extended):
- Add persistence (save/load trips)
- Integrate APIs for hotels/flights
- Add GUI or web interface
- Add advanced planning modules (transportation, day-wise schedule)

## Target users
- Students building small projects (course assignments)
- Beginner travelers who want a quick itinerary sketch tool
- Developers learning Python CLI applications and basic project structure

## High-level features
1. **Trip creation** : Enter destination, travel dates, budget and activities.
2. **Activity suggestions** : Show popular activities for a chosen destination (from a built-in list).
3. **Itinerary view** :Display the planned trip details in a readable format.
4. **Menu-driven interface** : Simple 3-option menu (Plan, View, Exit).

## Functional requirements (mapped to modules)
1. **User Input Module**
   - Accepts user input for destination, dates, budget, activities.
   - Validates basic input formats (numeric budget, destination exists).
2. **Suggestions Module**
   - Looks up and prints popular activities for supported destinations from an internal dictionary.
3. **Itinerary Module**
   - Stores current itinerary in memory and displays it when requested.

## Non-functional requirements
- **Usability:** The CLI menu must be clear and straightforward for first-time users.
- **Reliability:** The system should handle invalid input gracefully (e.g., non-numeric budget).
- **Maintainability:** Code should be modular to allow easy extension (separate functions/classes).
- **Performance:** Instant response for operations — negligible latency since operations are local/in-memory.
- **Extensibility:** Easy to add new destinations, persist data, or migrate to GUI/web front-end.

