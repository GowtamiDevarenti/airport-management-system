"""
==============================================================================
Lab 3 – Challenge: Airport Departure Management System
==============================================================================
Course: University Programming Lab (Python)
Student Project: Console-based Airport Departure Management System

This program simulates an airport departure management system for a small
regional airport. It manages flight departures, dynamic flight statuses,
passenger capacities, terminal gates, interactive flight searches, and
operational statistics/reports.

Python concepts demonstrated:
- Variables & basic calculations
- Data structures: Lists and Dictionaries
- Control flow: if / elif / else conditionals
- Loops: for loops and while loops
- Built-in helpers: range() and enumerate()
- Loop control: break and continue
- Functions for modular, readable code
==============================================================================
"""


# ============================================================================
# PART 1 & PART 6: FLIGHT DATA INITIALIZATION
# ============================================================================
# We use a LIST of DICTIONARIES to store flight information.
# A list maintains the ordered collection of flights.
# Each dictionary represents a single flight with descriptive key-value pairs:
#   - 'flight_number' : string identifier (e.g., 'SK142')
#   - 'destination'   : destination city (e.g., 'London')
#   - 'departure_time': scheduled departure time in 24h format (e.g., '14:30')
#   - 'gate'          : assigned gate (e.g., 'B4'), or None if unassigned
#   - 'passengers'    : current number of passengers booked (integer)
#   - 'max_capacity'  : maximum passenger capacity of the aircraft (integer)
#   - 'delay'         : delay in minutes (0 means on time)
#   - 'cancelled'     : boolean flag (True if flight is cancelled)
#
# Special cases included:
#   1. Cancelled flights: BA442, DY920
#   2. Flight without an assigned gate: AF118 (gate is None)
#   3. Flight with 0 passengers: KL601 (empty aircraft repositioning)
# ============================================================================

flights = [
    {
        "flight_number": "SK142",
        "destination": "London",
        "departure_time": "14:30",
        "gate": "B4",
        "passengers": 176,
        "max_capacity": 180,
        "delay": 25,
        "cancelled": False,
    },
    {
        "flight_number": "LH231",
        "destination": "Berlin",
        "departure_time": "15:00",
        "gate": "A2",
        "passengers": 150,
        "max_capacity": 180,
        "delay": 0,
        "cancelled": False,
    },
    {
        "flight_number": "BA442",
        "destination": "Manchester",
        "departure_time": "15:20",
        "gate": "C1",
        "passengers": 120,
        "max_capacity": 150,
        "delay": 0,
        "cancelled": True,  # Edge case: Cancelled flight
    },
    {
        "flight_number": "AF118",
        "destination": "Paris",
        "departure_time": "15:45",
        "gate": None,  # Edge case: Gate not assigned yet
        "passengers": 135,
        "max_capacity": 180,
        "delay": 65,  # Severely delayed (>= 60 mins)
        "cancelled": False,
    },
    {
        "flight_number": "KL601",
        "destination": "Amsterdam",
        "departure_time": "16:10",
        "gate": "B2",
        "passengers": 0,  # Edge case: 0 passengers (repositioning/ferry flight)
        "max_capacity": 100,
        "delay": 0,
        "cancelled": False,
    },
    {
        "flight_number": "AY854",
        "destination": "Helsinki",
        "departure_time": "16:30",
        "gate": "A1",
        "passengers": 110,
        "max_capacity": 180,
        "delay": 15,  # Slight delay (1 - 19 mins)
        "cancelled": False,
    },
    {
        "flight_number": "BA221",
        "destination": "Manchester",
        "departure_time": "17:00",
        "gate": "C3",
        "passengers": 160,
        "max_capacity": 190,
        "delay": 0,
        "cancelled": False,
    },
    {
        "flight_number": "IB310",
        "destination": "Madrid",
        "departure_time": "17:15",
        "gate": "A4",
        "passengers": 130,
        "max_capacity": 180,
        "delay": 0,
        "cancelled": False,
    },
    {
        "flight_number": "AZ402",
        "destination": "Rome",
        "departure_time": "17:40",
        "gate": "B1",
        "passengers": 140,
        "max_capacity": 180,
        "delay": 70,  # Severely delayed (>= 60 mins)
        "cancelled": False,
    },
    {
        "flight_number": "DY920",
        "destination": "Oslo",
        "departure_time": "18:00",
        "gate": "C2",
        "passengers": 126,
        "max_capacity": 180,
        "delay": 0,
        "cancelled": True,  # Edge case: Cancelled flight
    },
]


# ============================================================================
# PART 3: DETERMINE FLIGHT STATUS DYNAMICALLY
# ============================================================================
# The status of each flight is calculated dynamically based on specific rules:
#   1. Cancelled           -> "CANCELLED" (checked first regardless of delay)
#   2. Delay >= 60 minutes -> "SEVERELY DELAYED"
#   3. Delay 20-59 minutes -> "DELAYED"
#   4. Delay 1-19 minutes  -> "SLIGHT DELAY"
#   5. No delay (0 mins)   -> "ON TIME"
#
# DESIGN NOTE (Design Challenge Improvement 1):
# By checking `cancelled` first, we guarantee that cancelled flights are
# never mislabeled as delayed even if a delay value is present.
# Checking delays in descending order (>= 60, then >= 20, then > 0)
# simplifies logic by eliminating redundant compound ranges (e.g., delay >= 20
# and delay < 60).
# ============================================================================

def get_flight_status(flight):
    """
    Dynamically computes and returns the status string for a given flight dictionary.
    """
    if flight["cancelled"]:
        return "CANCELLED"
    elif flight["delay"] >= 60:
        return "SEVERELY DELAYED"
    elif flight["delay"] >= 20:
        return "DELAYED"
    elif flight["delay"] > 0:
        return "SLIGHT DELAY"
    else:
        return "ON TIME"


def format_gate(gate_value):
    """
    Helper function to format the gate display.
    If the gate is None or empty, returns 'Gate not assigned' as required by Part 6.
    Otherwise, returns 'Gate <gate_value>'.
    """
    if gate_value is None or gate_value == "":
        return "Gate not assigned"
    return f"Gate {gate_value}"


# ============================================================================
# PART 7: GATE OVERVIEW GENERATION
# ============================================================================
# The airport contains:
#   - 3 terminals: A, B, C
#   - 4 gate numbers per terminal: 1, 2, 3, 4
#
# We generate all 12 combinations programmatically using nested for loops
# and range(1, 5). No manual hardcoding of all twelve gates.
# ============================================================================

def display_gate_overview():
    """
    Generates and displays all possible airport gate combinations
    using nested for loops and range().
    """
    print("\n--- AIRPORT GATE OVERVIEW ---")
    terminals = ["A", "B", "C"]  # List of terminal letters

    for terminal in terminals:
        # range(1, 5) generates gate numbers 1, 2, 3, 4
        for gate_number in range(1, 5):
            gate_code = terminal + str(gate_number)
            print(f"Gate {gate_code}")
    print("-----------------------------\n")


# ============================================================================
# PART 2 & PART 8 (OPTIONS 1, 2, 3): DEPARTURE BOARDS
# ============================================================================
# Functions to display flight departure information.
# enumerate() is used to automatically number the flights (starting at index 1).
# ============================================================================

def display_all_flights():
    """
    Option 1: Display all scheduled flights.
    Uses enumerate() with start=1 to automatically number the flights.
    """
    print("\n" + "=" * 65)
    print("                ALL SCHEDULED DEPARTURES")
    print("=" * 65)

    # Use enumerate() to automatically generate flight sequence numbers
    for index, flight in enumerate(flights, start=1):
        status = get_flight_status(flight)
        gate_text = format_gate(flight["gate"])
        
        # Display flight details
        line = f"{index}. {flight['flight_number']} - {flight['destination']} - {flight['departure_time']} - {gate_text}"
        print(f"{line:<48} | Status: {status}")

    print("=" * 65 + "\n")


def display_delayed_flights():
    """
    Option 2: Display only flights that have a delay.
    Per Part 8 specification: Cancelled flights should NOT be included in this view.
    Demonstrates the genuine use of `continue` to skip irrelevant records.
    """
    print("\n" + "=" * 65)
    print("                    DELAYED FLIGHTS")
    print("=" * 65)

    delayed_found = False
    display_index = 1

    for flight in flights:
        # Part 9 concept: Use continue to skip flights that are cancelled
        if flight["cancelled"]:
            continue

        # Skip flights with zero delay
        if flight["delay"] == 0:
            continue

        delayed_found = True
        status = get_flight_status(flight)
        gate_text = format_gate(flight["gate"])
        delay_info = f"({flight['delay']} min delay)"

        line = f"{display_index}. {flight['flight_number']} - {flight['destination']} - {flight['departure_time']} - {gate_text}"
        print(f"{line:<48} | Status: {status} {delay_info}")
        display_index += 1

    if not delayed_found:
        print("No delayed flights at this time.")

    print("=" * 65 + "\n")


def display_cancelled_flights():
    """
    Option 3: Display only cancelled flights.
    Demonstrates the genuine use of `continue` to skip active flights.
    """
    print("\n" + "=" * 65)
    print("                   CANCELLED FLIGHTS")
    print("=" * 65)

    cancelled_found = False
    display_index = 1

    for flight in flights:
        # Skip active flights using continue
        if not flight["cancelled"]:
            continue

        cancelled_found = True
        gate_text = format_gate(flight["gate"])
        line = f"{display_index}. {flight['flight_number']} - {flight['destination']} - {flight['departure_time']} - {gate_text}"
        print(f"{line:<48} | Status: CANCELLED")
        display_index += 1

    if not cancelled_found:
        print("No flights are currently cancelled.")

    print("=" * 65 + "\n")


# ============================================================================
# PART 5: SEARCH FOR A FLIGHT
# ============================================================================
# Allows user to look up a flight by its flight number.
#
# Key concepts:
#   - Input handling (converted to uppercase for case-insensitive matching)
#   - Boolean `found` flag to determine if a match was identified
#   - `break` statement: once the flight is found, stop searching through
#     the remaining flights immediately (avoids unnecessary iterations)
# ============================================================================

def search_flight():
    """
    Option 4: Search for a flight by its flight number.
    Uses a for loop with a break statement and a boolean found flag.
    """
    search_code = input("\nEnter flight number: ").strip().upper()

    found = False  # Flag to track whether matching flight was located

    for flight in flights:
        if flight["flight_number"].upper() == search_code:
            found = True
            status = get_flight_status(flight)
            gate_text = format_gate(flight["gate"])

            print("\nFlight Details Found:")
            print("-" * 30)
            print(f"Flight Number : {flight['flight_number']}")
            print(f"Destination   : {flight['destination']}")
            print(f"Departure     : {flight['departure_time']}")
            print(f"Gate          : {gate_text}")
            print(f"Passengers    : {flight['passengers']} / {flight['max_capacity']}")
            print(f"Status        : {status}")
            if flight["delay"] > 0 and not flight["cancelled"]:
                print(f"Delay         : {flight['delay']} minutes")
            print("-" * 30 + "\n")

            # Part 9 concept: stop searching immediately once flight is found
            break

    if not found:
        print(f"\nFlight not found: '{search_code}'. Please verify the flight number.\n")


# ============================================================================
# PART 4 & FINAL CHALLENGE: FLIGHT ANALYSIS & AIRPORT OPERATIONS REPORT
# ============================================================================
# Calculates and displays operational airport statistics.
#
# CONSTRAINTS & RULES:
#   1. "Do not use max() to find the flight with the largest number of passengers.
#       Your program should determine it while processing the data."
#   2. "Flights with 0 passengers should not be included when calculating the
#       average passenger count for active flights."
#   3. Delayed flights count represents active (non-cancelled) flights with delay > 0.
#   4. On-time flights count represents active flights with delay == 0.
#   5. Flights above 80% capacity checks (passengers / max_capacity) > 0.80.
# ============================================================================

def calculate_flight_statistics():
    """
    Performs manual calculations across the flight data.
    Returns a dictionary of all aggregated metrics for reuse in
    both Option 5 (statistics view) and Option 6 (operations report).
    """
    total_scheduled = len(flights)
    cancelled_count = 0
    delayed_count = 0
    ontime_count = 0
    total_passengers = 0

    # For average passenger count on active flights (excluding 0-passenger flights)
    active_flight_passengers = 0
    active_flight_count = 0

    # Manual search for busiest flight (DO NOT USE max())
    busiest_flight = None
    max_passengers = -1

    # Flights above 80% capacity
    high_capacity_flights = []

    # Additional analysis metrics
    total_delay_minutes = 0
    longest_delay_flight = None
    longest_delay_minutes = -1

    # Dictionary to track destination passenger totals
    destination_passengers = {}

    for flight in flights:
        # Sum total passengers booked across all scheduled flights
        total_passengers += flight["passengers"]

        # Track destination passenger volumes for additional analysis
        dest = flight["destination"]
        if dest in destination_passengers:
            destination_passengers[dest] += flight["passengers"]
        else:
            destination_passengers[dest] = flight["passengers"]

        # Manual determination of busiest flight (strictly avoiding max())
        if flight["passengers"] > max_passengers:
            max_passengers = flight["passengers"]
            busiest_flight = flight

        # Check for flights operating above 80% capacity (> 0.80)
        capacity_ratio = flight["passengers"] / flight["max_capacity"]
        if capacity_ratio > 0.80:
            high_capacity_flights.append(flight)

        # Classify flight operational state
        if flight["cancelled"]:
            cancelled_count += 1
            # Cancelled flights are not counted as delayed or on-time
            continue

        # Below this point, the flight is ACTIVE (not cancelled)
        if flight["delay"] > 0:
            delayed_count += 1
            total_delay_minutes += flight["delay"]

            # Track longest delayed flight manually
            if flight["delay"] > longest_delay_minutes:
                longest_delay_minutes = flight["delay"]
                longest_delay_flight = flight
        else:
            ontime_count += 1

        # Calculate active flights average passenger count
        # Part 6 rule: flights with 0 passengers should not be included
        if flight["passengers"] == 0:
            continue

        active_flight_passengers += flight["passengers"]
        active_flight_count += 1

    # Calculate average passengers for active flights (with > 0 passengers)
    if active_flight_count > 0:
        avg_passengers_active = round(active_flight_passengers / active_flight_count, 1)
    else:
        avg_passengers_active = 0.0

    # Calculate average delay among delayed flights
    if delayed_count > 0:
        avg_delay_minutes = round(total_delay_minutes / delayed_count, 1)
    else:
        avg_delay_minutes = 0.0

    # Calculate cancellation percentage
    if total_scheduled > 0:
        cancellation_percentage = round((cancelled_count / total_scheduled) * 100, 1)
    else:
        cancellation_percentage = 0.0

    # Find destination with most passengers manually without max()
    top_destination = None
    top_dest_passengers = -1
    for dest, count in destination_passengers.items():
        if count > top_dest_passengers:
            top_dest_passengers = count
            top_destination = dest

    return {
        "total_scheduled": total_scheduled,
        "cancelled_count": cancelled_count,
        "delayed_count": delayed_count,
        "ontime_count": ontime_count,
        "total_passengers": total_passengers,
        "avg_passengers_active": avg_passengers_active,
        "active_flight_count": active_flight_count,
        "busiest_flight": busiest_flight,
        "high_capacity_flights": high_capacity_flights,
        "avg_delay_minutes": avg_delay_minutes,
        "longest_delay_flight": longest_delay_flight,
        "longest_delay_minutes": longest_delay_minutes,
        "cancellation_percentage": cancellation_percentage,
        "top_destination": top_destination,
        "top_dest_passengers": top_dest_passengers,
    }


def display_flight_statistics():
    """
    Option 5: Display flight statistics (Part 4 requirements).
    """
    stats = calculate_flight_statistics()

    print("\n" + "=" * 55)
    print("               FLIGHT STATISTICS OVERVIEW")
    print("=" * 55)
    print(f"Total scheduled flights             : {stats['total_scheduled']}")
    print(f"Number of cancelled flights         : {stats['cancelled_count']}")
    print(f"Number of delayed flights           : {stats['delayed_count']}")
    print(f"Number of flights departing on time : {stats['ontime_count']}")
    print(f"Total number of passengers          : {stats['total_passengers']}")
    print(f"Average passengers per active flight: {stats['avg_passengers_active']} (excl. 0-pax flights)")
    
    busiest = stats["busiest_flight"]
    if busiest:
        print(f"Busiest flight (manual search)      : {busiest['flight_number']} - {busiest['destination']} ({busiest['passengers']} passengers)")
    
    print(f"Flights with > 80% capacity filled  : {len(stats['high_capacity_flights'])}")
    for f in stats["high_capacity_flights"]:
        pct = round((f["passengers"] / f["max_capacity"]) * 100, 1)
        print(f"  * {f['flight_number']} - {f['destination']} ({f['passengers']}/{f['max_capacity']} - {pct}%)")
    print("=" * 55 + "\n")


def display_airport_operations_report():
    """
    Option 6: Airport Operations Report (Final Challenge).
    Formats the summary output according to the PDF's exact template
    and presents additional analyses.
    """
    stats = calculate_flight_statistics()

    print("\n" + "-" * 40)
    print("AIRPORT OPERATIONS REPORT")
    print("-" * 40)
    print(f"Scheduled flights: {stats['total_scheduled']}")
    print(f"Cancelled flights: {stats['cancelled_count']}")
    print(f"Delayed flights: {stats['delayed_count']}")
    print(f"On-time flights: {stats['ontime_count']}\n")

    print(f"Passengers today: {stats['total_passengers']}\n")

    busiest = stats["busiest_flight"]
    print("Busiest flight:")
    if busiest:
        print(f"{busiest['flight_number']} - {busiest['destination']} - {busiest['passengers']} passengers\n")

    print("Flights above 80% capacity:")
    for f in stats["high_capacity_flights"]:
        print(f"{f['flight_number']} - {f['destination']}")

    print("\n" + "-" * 40)
    print("ADDITIONAL OPERATIONAL ANALYSIS")
    print("-" * 40)
    print(f"* Cancellation Rate            : {stats['cancellation_percentage']}%")
    print(f"* Average Delay (delayed flights): {stats['avg_delay_minutes']} minutes")
    if stats["longest_delay_flight"]:
        ld = stats["longest_delay_flight"]
        print(f"* Longest Delay                : {ld['flight_number']} to {ld['destination']} ({ld['delay']} minutes)")
    print(f"* Most Popular Destination     : {stats['top_destination']} ({stats['top_dest_passengers']} total passengers)")
    print("-" * 40 + "\n")


# ============================================================================
# PART 8: INTERACTIVE AIRPORT MENU
# ============================================================================
# Repeatedly displays the main menu using a while loop until the user quits.
# Handles invalid choices gracefully.
# Uses `break` to exit the loop when option 8 (Quit) is selected.
# ============================================================================

def main_menu():
    """
    Continuously running interactive console menu using a while loop.
    """
    while True:
        print("========================================")
        print("        AIRPORT DEPARTURE SYSTEM")
        print("========================================")
        print("1. View all flights")
        print("2. View delayed flights")
        print("3. View cancelled flights")
        print("4. Search for a flight")
        print("5. View flight statistics")
        print("6. Airport Operations Report")
        print("7. Gate overview")
        print("8. Quit")
        print("========================================")

        choice = input("Choose an option: ").strip()

        # Branching using if / elif / else
        if choice == "1":
            display_all_flights()
        elif choice == "2":
            display_delayed_flights()
        elif choice == "3":
            display_cancelled_flights()
        elif choice == "4":
            search_flight()
        elif choice == "5":
            display_flight_statistics()
        elif choice == "6":
            display_airport_operations_report()
        elif choice == "7":
            display_gate_overview()
        elif choice == "8" or choice.lower() in ["quit", "q", "exit"]:
            print("\nThank you for using the Airport Departure System. Goodbye!\n")
            # Genuine use of break to terminate the interactive menu loop
            break
        else:
            print(f"\n[ERROR] Invalid choice '{choice}'. Please select a valid option (1-8).\n")


# Program entry point
if __name__ == "__main__":
    main_menu()
