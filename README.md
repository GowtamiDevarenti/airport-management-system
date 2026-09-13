# Airport Departure Management System

**Course:** University Python Programming Lab  
**Assignment:** Lab 3 – Challenge: Airport Departure Management System  
**Language:** Python 3 (Pure standard library, beginner-friendly)  

---

## 1. Project Description

The **Airport Departure Management System** is a console-based application designed to simulate departure operations at a regional airport. The system models realistic flight schedules, dynamically classifies flight statuses, calculates operational metrics, generates terminal gate combinations, supports real-time flight search, and presents a complete **Airport Operations Report**.

The project is structured specifically for university students learning fundamental Python programming concepts, avoiding complex object-oriented patterns or third-party libraries in favor of foundational data structures (lists and dictionaries), standard control flow, and clean functional organization.

---

## 2. How to Run the Program

### Prerequisites
- Python 3.8 or higher installed on your computer.
- **No external dependencies required** (uses only Python's built-in standard library).

### Execution Commands

To launch the interactive application:

```bash
# Navigate to the project directory
cd "airport-management-system"

# Run the program
python main.py
```

To run the automated test verification suite:

```bash
python test_airport_system.py
```

---

## 3. System Features

The program provides an interactive, menu-driven console interface with the following core features:

1. **View All Scheduled Departures**: Displays all flights auto-numbered using `enumerate()`, showing flight number, destination city, departure time, assigned gate, and dynamically evaluated status.
2. **View Delayed Flights**: Filters and displays active flights experiencing delays, skipping on-time and cancelled flights.
3. **View Cancelled Flights**: Filters and displays flights that are marked as cancelled.
4. **Search for a Flight**: Prompts for a flight number, performs a case-insensitive search, displays matching details, and terminates search immediately using `break`.
5. **View Flight Statistics**: Calculates key operational metrics, including scheduled flights, cancelled flights, delayed flights, on-time flights, total passengers, average passengers per active flight (excluding 0-passenger flights), the busiest flight (computed manually without `max()`), and flights exceeding 80% capacity.
6. **Airport Operations Report**: Extends the statistics into a formatted management summary matching the laboratory specification, with additional operational analyses (cancellation percentage, average delay, longest delay, and most popular destination).
7. **Gate Overview**: Programmatically generates and displays all airport gate combinations across Terminals A, B, and C with gates 1–4 using nested `for` loops and `range()`.
8. **Quit**: Gracefully exits the application with a goodbye message.

---

## 4. Python Concepts Demonstrated

The program explicitly demonstrates core beginner Python constructs:

| Concept | Description | Where Used in Code |
| :--- | :--- | :--- |
| **Variables & Calculations** | Numeric sums, percentage ratios, roundings, and string operations | Capacity ratios, cancellation rates, passenger totals |
| **Lists** | Ordered collections of flights and terminal identifiers | `flights = [...]`, `terminals = ["A", "B", "C"]` |
| **Dictionaries** | Key-value pairs representing individual flight attributes | Each flight entry in `flights` list |
| **`if / elif / else`** | Priority-based conditional branching | `get_flight_status()`, menu choices, capacity checks |
| **`for` loops** | Sequential iteration over collections | Iterating through flights, terminals, and gate numbers |
| **`while` loops** | Continuous interactive execution until user exit | `main_menu()` interactive loop |
| **`range()`** | Generating numeric sequences programmatically | `range(1, 5)` in `display_gate_overview()` |
| **`enumerate()`** | Automatic 1-indexed numbering of displayed items | `display_all_flights()` departure board |
| **`break`** | Early loop termination | Terminating `search_flight()` when found, exiting menu |
| **`continue`** | Skipping irrelevant loop iterations | Skipping cancelled / 0-passenger flights in calculations |
| **Functions** | Reusable, modular logic blocks | `get_flight_status()`, `calculate_flight_statistics()` |

---

## 5. Flight Data & Special Case Handling

The dataset consists of 10 realistic flights designed to accurately produce the exact numbers from the PDF sample report:

```python
flights = [
    {"flight_number": "SK142", "destination": "London",     "departure_time": "14:30", "gate": "B4",  "passengers": 176, "max_capacity": 180, "delay": 25, "cancelled": False},
    {"flight_number": "LH231", "destination": "Berlin",     "departure_time": "15:00", "gate": "A2",  "passengers": 150, "max_capacity": 180, "delay": 0,  "cancelled": False},
    {"flight_number": "BA442", "destination": "Manchester", "departure_time": "15:20", "gate": "C1",  "passengers": 120, "max_capacity": 150, "delay": 0,  "cancelled": True},
    {"flight_number": "AF118", "destination": "Paris",      "departure_time": "15:45", "gate": None,  "passengers": 135, "max_capacity": 180, "delay": 65, "cancelled": False},
    {"flight_number": "KL601", "destination": "Amsterdam",  "departure_time": "16:10", "gate": "B2",  "passengers": 0,   "max_capacity": 100, "delay": 0,  "cancelled": False},
    {"flight_number": "AY854", "destination": "Helsinki",   "departure_time": "16:30", "gate": "A1",  "passengers": 110, "max_capacity": 180, "delay": 15, "cancelled": False},
    {"flight_number": "BA221", "destination": "Manchester", "departure_time": "17:00", "gate": "C3",  "passengers": 160, "max_capacity": 190, "delay": 0,  "cancelled": False},
    {"flight_number": "IB310", "destination": "Madrid",     "departure_time": "17:15", "gate": "A4",  "passengers": 130, "max_capacity": 180, "delay": 0,  "cancelled": False},
    {"flight_number": "AZ402", "destination": "Rome",       "departure_time": "17:40", "gate": "B1",  "passengers": 140, "max_capacity": 180, "delay": 70, "cancelled": False},
    {"flight_number": "DY920", "destination": "Oslo",       "departure_time": "18:00", "gate": "C2",  "passengers": 126, "max_capacity": 180, "delay": 0,  "cancelled": True},
]
```

### Edge Cases Handled:
1. **Cancelled Flights (`BA442`, `DY920`)**:
   - Status always resolves to `"CANCELLED"` regardless of delay.
   - Cancelled flights are excluded from delayed and on-time flight counts, and are not shown in "View delayed flights".
2. **Unassigned Gate (`AF118`)**:
   - Represented as `gate: None`.
   - Handled via `format_gate()` to display `"Gate not assigned"` instead of `"None"`.
3. **Zero-Passenger Flight (`KL601`)**:
   - Represents an empty positioning / ferry flight.
   - Excluded from the active flight average passenger calculation using `continue`, ensuring the denominator is not skewed.

---

## 6. Airport Operations Report & Additional Analysis

The **Airport Operations Report** produces the following exact output:

```text
----------------------------------------
AIRPORT OPERATIONS REPORT
----------------------------------------
Scheduled flights: 10
Cancelled flights: 2
Delayed flights: 4
On-time flights: 4

Passengers today: 1247

Busiest flight:
SK142 - London - 176 passengers

Flights above 80% capacity:
SK142 - London
LH231 - Berlin
BA221 - Manchester

----------------------------------------
ADDITIONAL OPERATIONAL ANALYSIS
----------------------------------------
* Cancellation Rate            : 20.0%
* Average Delay (delayed flights): 43.8 minutes
* Longest Delay                : AZ402 to Rome (70 minutes)
* Most Popular Destination     : London (176 total passengers)
----------------------------------------
```

### Calculation Verification:
- **Total Passengers**: $176 + 150 + 120 + 135 + 0 + 110 + 160 + 130 + 140 + 126 = 1,247$
- **Average Passengers per Active Flight**: Active flights with $> 0$ passengers $= 7$ (excluding cancelled flights BA442 & DY920, and 0-passenger flight KL601). Total active passengers $= 1,001$. Average $= 1001 / 7 = 143.0$.
- **Busiest Flight**: `SK142` to London ($176$ passengers), determined via manual comparison loop without `max()`.
- **Flights above 80% Capacity**:
  - `SK142`: $176 / 180 = 97.8\% > 80\%$
  - `LH231`: $150 / 180 = 83.3\% > 80\%$
  - `BA221`: $160 / 190 = 84.2\% > 80\%$

---

## 7. Design Challenge: Solutions & Improvements

Per the specification, here are four explicit design improvements over naive student approaches:

### Improvement 1: Flight Status Classification Condition Ordering
- **Original approach:** The naive solution checked delay thresholds first (e.g., `if delay >= 60: ... elif delay >= 20: ...`) and only checked `if cancelled:` at the end or in a separate statement. If a flight had a 30-minute delay and was subsequently cancelled, it was mistakenly classified as `"DELAYED"`.
- **Improved approach:** Placed `if flight["cancelled"]:` as the very first check with highest priority. Then, delay checks were ordered in strict descending numerical order (`>= 60`, then `>= 20`, then `> 0`, with an `else` branch for `"ON TIME"`).
- **Why it is better:** Guarantees that the critical safety rule—*a cancelled flight must always display "CANCELLED" regardless of delay*—is never violated. Descending order also removes the need for redundant compound boolean checks (e.g. `delay >= 20 and delay < 60`), making the code cleaner and less error-prone.

### Improvement 2: Modular Gate Display Formatting
- **Original approach:** In each flight display loop (all flights, delayed flights, cancelled flights, search), the code repeatedly checked `if flight["gate"] is None: ... else: ...` with repetitive string concatenations.
- **Improved approach:** Encapsulated the gate display logic into a single reusable helper function `format_gate(gate_value)`.
- **Why it is better:** Enforces DRY (Don't Repeat Yourself). Eliminates code duplication across 4 different functions and guarantees consistent representation (`"Gate not assigned"`) everywhere in the application.

### Improvement 3: Single-Pass Manual Statistics with `continue` vs Forbidden `max()`
- **Original approach:** A naive implementation used Python's built-in `max()` function (violating the lab rules) or iterated through the flight list multiple times to calculate separate totals. It also included 0-passenger flights in the active passenger denominator, distorting the average.
- **Improved approach:** A single `for` loop aggregates totals, checks capacity percentages, tracks destination volumes, and determines the busiest flight manually (`if flight["passengers"] > max_passengers:`). `continue` statements cleanly filter out cancelled and 0-passenger flights.
- **Why it is better:** Strictly adheres to assignment constraints, handles edge cases accurately, and achieves optimal $O(N)$ efficiency in a single pass.

### Improvement 4: Programmatic Gate Generation using Nested Loops and `range()`
- **Original approach:** Manually hardcoding a static list of 12 gate strings: `["A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4", "C1", "C2", "C3", "C4"]`.
- **Improved approach:** Generated gates dynamically using a list of terminal identifiers `["A", "B", "C"]` and `range(1, 5)` inside nested `for` loops.
- **Why it is better:** Avoids hardcoding, reduces human typographical errors, and easily scales if new terminals or additional gate numbers are added.

---

## 8. PDF Requirement Verification Checklist

The table below verifies the implementation against every requirement in the lab specification:

| PDF Section | Specification Requirement | Implemented? | Location in Codebase |
| :--- | :--- | :---: | :--- |
| **Part 1** | Collection containing at least 10 scheduled flights | **Yes** | `main.py` (lines 35–130) |
| **Part 1** | Flight attributes: number, destination, time, gate, pax, capacity, delay, cancelled | **Yes** | `main.py` (`flights` list dictionaries) |
| **Part 2** | Departure board displaying all flights with auto-numbering | **Yes** | `main.py` (`display_all_flights()`) |
| **Part 2** | Use `enumerate()` for numbering instead of manual prints | **Yes** | `main.py` (`display_all_flights()`) |
| **Part 3** | Flight status rules: CANCELLED, SEVERELY DELAYED, DELAYED, SLIGHT DELAY, ON TIME | **Yes** | `main.py` (`get_flight_status()`) |
| **Part 3** | Cancelled flight always displays CANCELLED regardless of delay | **Yes** | `main.py` (`get_flight_status()`) |
| **Part 4** | Total scheduled, cancelled, delayed, and on-time flight counts | **Yes** | `main.py` (`calculate_flight_statistics()`) |
| **Part 4** | Total passengers and average passengers per active flight | **Yes** | `main.py` (`calculate_flight_statistics()`) |
| **Part 4** | Flight with largest number of passengers determined manually without `max()` | **Yes** | `main.py` (`calculate_flight_statistics()`) |
| **Part 4** | Number of flights operating above 80% capacity | **Yes** | `main.py` (`calculate_flight_statistics()`) |
| **Part 5** | Flight search by flight number (case-insensitive) | **Yes** | `main.py` (`search_flight()`) |
| **Part 5** | Stop search immediately once found using `break` | **Yes** | `main.py` (`search_flight()`) |
| **Part 5** | Appropriate "Flight not found" message using boolean `found` flag | **Yes** | `main.py` (`search_flight()`) |
| **Part 6** | Include at least one cancelled flight | **Yes** | `main.py` (`BA442`, `DY920`) |
| **Part 6** | Include at least one flight with no gate (display "Gate not assigned") | **Yes** | `main.py` (`AF118`, `format_gate()`) |
| **Part 6** | Include at least one flight with 0 passengers (exclude from active average) | **Yes** | `main.py` (`KL601`, `calculate_flight_statistics()`) |
| **Part 7** | Generate all gates for Terminals A, B, C (1-4) with loops and `range()` | **Yes** | `main.py` (`display_gate_overview()`) |
| **Part 7** | Do not manually hardcode all 12 gate combinations | **Yes** | `main.py` (`display_gate_overview()`) |
| **Part 8** | Interactive menu continuously running with `while` loop | **Yes** | `main.py` (`main_menu()`) |
| **Part 8** | Menu options: All flights, Delayed flights, Cancelled flights, Search, Statistics, Quit | **Yes** | `main.py` (`main_menu()`) |
| **Part 8** | Cancelled flights excluded from "View delayed flights" | **Yes** | `main.py` (`display_delayed_flights()`) |
| **Part 8** | Graceful handling of invalid menu options with error message | **Yes** | `main.py` (`main_menu()`) |
| **Part 9** | Genuine use of `break` (search termination and menu exit) | **Yes** | `main.py` (`search_flight()`, `main_menu()`) |
| **Part 9** | Genuine use of `continue` (skipping cancelled / 0-pax flights) | **Yes** | `main.py` (`calculate_flight_statistics()`) |
| **Final Challenge** | Airport Operations Report matching specification format | **Yes** | `main.py` (`display_airport_operations_report()`) |
| **Final Challenge** | Additional operational analysis (cancellation %, avg delay, longest delay, destination) | **Yes** | `main.py` (`display_airport_operations_report()`) |
| **Design Challenge** | Document at least two explicit improvements with Original / Changed / Why better | **Yes** | `README.md` (Section 7) and `main.py` comments |

---

## 9. Testing Summary

An automated test suite (`test_airport_system.py`) was executed to validate the implementation.

### Test Results:
1. **Data Integrity Test:** PASSED. Verified 10 scheduled flights with all 8 required dictionary keys, 2 cancelled flights, 1 unassigned gate flight, and 1 zero-passenger flight.
2. **Status Classification Test:** PASSED. Verified all 5 status classifications and confirmed cancelled status overrides delay values.
3. **Statistics & Calculations Test:** PASSED. Verified exact numerical metrics:
   - Total scheduled: 10
   - Cancelled: 2
   - Delayed: 4
   - On-time: 4
   - Total passengers: 1,247
   - Average active passengers: 143.0
   - Busiest flight: `SK142` with 176 passengers (computed without `max()`)
   - High capacity (> 80%): 3 flights (`SK142`, `LH231`, `BA221`)
4. **Gate Generation Test:** PASSED. Verified that all 12 gate combinations (A1–C4) are generated programmatically via nested loops and `range()`.
5. **Interactive Menu & Error Handling Test:** PASSED. Tested all menu paths (1–8), case-insensitive search (`sk142`), missing flight lookup (`ZZ999`), invalid numeric input recovery (`99`), and clean exit on option `8`.

---

## 10. Design Assumptions & Notes

- **Delayed vs Cancelled Classification:** In alignment with Part 8 ("Cancelled flights should not be included in this view"), delayed flight counts and the delayed flight view consider only active (non-cancelled) flights with delays $> 0$.
- **Active Flight Definition for Passenger Average:** Per Part 6 ("flights with 0 passengers should not be included when calculating the average passenger count for active flights"), the average passenger metric divides total passengers on non-cancelled flights with $> 0$ passengers by the count of those active flights ($1,001 / 7 = 143.0$).
- **Flight Search Case-Insensitivity:** Users can enter flight numbers in lower or upper case (e.g., `sk142` or `SK142`), and leading/trailing whitespace is stripped for user convenience.
