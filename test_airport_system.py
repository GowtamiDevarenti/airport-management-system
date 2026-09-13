"""
Automated Test Suite for Airport Departure Management System
Tests all functions, edge cases, calculations, and the interactive menu.
"""
import io
import sys
import os

# Import main from the current directory
import main

def test_flight_data_integrity():
    print("Testing Part 1 & 6: Flight Data Integrity...")
    assert len(main.flights) >= 10, f"Expected at least 10 flights, got {len(main.flights)}"
    
    cancelled_count = 0
    no_gate_count = 0
    zero_pax_count = 0
    
    for f in main.flights:
        assert "flight_number" in f
        assert "destination" in f
        assert "departure_time" in f
        assert "gate" in f
        assert "passengers" in f
        assert "max_capacity" in f
        assert "delay" in f
        assert "cancelled" in f
        
        if f["cancelled"]:
            cancelled_count += 1
        if f["gate"] is None or f["gate"] == "":
            no_gate_count += 1
        if f["passengers"] == 0:
            zero_pax_count += 1
            
    assert cancelled_count >= 1, "Expected at least 1 cancelled flight"
    assert no_gate_count >= 1, "Expected at least 1 flight with no gate"
    assert zero_pax_count >= 1, "Expected at least 1 flight with 0 passengers"
    print(f"  [PASS] Data integrity verified: {len(main.flights)} flights, {cancelled_count} cancelled, {no_gate_count} unassigned gate, {zero_pax_count} zero-pax.")

def test_flight_status_classification():
    print("\nTesting Part 3: Flight Status Classification Rules...")
    # 1. Cancelled regardless of delay
    assert main.get_flight_status({"cancelled": True, "delay": 0}) == "CANCELLED"
    assert main.get_flight_status({"cancelled": True, "delay": 120}) == "CANCELLED"
    
    # 2. Delay >= 60 -> SEVERELY DELAYED
    assert main.get_flight_status({"cancelled": False, "delay": 60}) == "SEVERELY DELAYED"
    assert main.get_flight_status({"cancelled": False, "delay": 95}) == "SEVERELY DELAYED"
    
    # 3. Delay 20 - 59 -> DELAYED
    assert main.get_flight_status({"cancelled": False, "delay": 20}) == "DELAYED"
    assert main.get_flight_status({"cancelled": False, "delay": 59}) == "DELAYED"
    
    # 4. Delay 1 - 19 -> SLIGHT DELAY
    assert main.get_flight_status({"cancelled": False, "delay": 1}) == "SLIGHT DELAY"
    assert main.get_flight_status({"cancelled": False, "delay": 19}) == "SLIGHT DELAY"
    
    # 5. Delay 0 -> ON TIME
    assert main.get_flight_status({"cancelled": False, "delay": 0}) == "ON TIME"
    print("  [PASS] All status classification rules verified.")

def test_statistics_calculations():
    print("\nTesting Part 4, 6 & Final Challenge: Statistics & Operations Report...")
    stats = main.calculate_flight_statistics()
    
    # Check counts
    assert stats["total_scheduled"] == 10, f"Expected 10 total scheduled, got {stats['total_scheduled']}"
    assert stats["cancelled_count"] == 2, f"Expected 2 cancelled flights, got {stats['cancelled_count']}"
    assert stats["delayed_count"] == 4, f"Expected 4 delayed flights, got {stats['delayed_count']}"
    assert stats["ontime_count"] == 4, f"Expected 4 on-time flights, got {stats['ontime_count']}"
    assert stats["total_scheduled"] == stats["cancelled_count"] + stats["delayed_count"] + stats["ontime_count"]
    
    # Check passenger sums
    assert stats["total_passengers"] == 1247, f"Expected 1247 total passengers, got {stats['total_passengers']}"
    
    # Check active flight average passenger count (excluding 0-passenger flights)
    # Active flights with > 0 pax: 7 flights, sum = 1001. 1001 / 7 = 143.0
    assert stats["active_flight_count"] == 7, f"Expected 7 active flights with > 0 pax, got {stats['active_flight_count']}"
    assert stats["avg_passengers_active"] == 143.0, f"Expected 143.0 avg passengers, got {stats['avg_passengers_active']}"
    
    # Check busiest flight (manually calculated, no max())
    busiest = stats["busiest_flight"]
    assert busiest is not None
    assert busiest["flight_number"] == "SK142"
    assert busiest["destination"] == "London"
    assert busiest["passengers"] == 176
    
    # Check flights above 80% capacity
    high_cap = stats["high_capacity_flights"]
    assert len(high_cap) == 3, f"Expected 3 high capacity flights, got {len(high_cap)}"
    high_cap_nums = [f["flight_number"] for f in high_cap]
    assert "SK142" in high_cap_nums
    assert "LH231" in high_cap_nums
    assert "BA221" in high_cap_nums
    
    # Check additional analysis metrics
    # Delayed delays: SK142(25), AF118(65), AY854(15), AZ402(70) -> Total = 175, Avg = 175 / 4 = 43.8
    assert stats["avg_delay_minutes"] == 43.8, f"Expected avg delay 43.8, got {stats['avg_delay_minutes']}"
    assert stats["longest_delay_minutes"] == 70, f"Expected longest delay 70, got {stats['longest_delay_minutes']}"
    assert stats["cancellation_percentage"] == 20.0, f"Expected cancellation 20.0%, got {stats['cancellation_percentage']}"
    
    print("  [PASS] All statistical calculations match expected values exactly!")

def test_gate_generation():
    print("\nTesting Part 7: Programmatic Gate Generation...")
    captured_output = io.StringIO()
    sys.stdout = captured_output
    try:
        main.display_gate_overview()
    finally:
        sys.stdout = sys.__stdout__
        
    out = captured_output.getvalue()
    expected_gates = [
        "Gate A1", "Gate A2", "Gate A3", "Gate A4",
        "Gate B1", "Gate B2", "Gate B3", "Gate B4",
        "Gate C1", "Gate C2", "Gate C3", "Gate C4",
    ]
    for gate in expected_gates:
        assert gate in out, f"Missing {gate} in gate overview"
    print("  [PASS] All 12 gates generated and verified programmatically.")

def test_interactive_menu_flow():
    print("\nTesting Part 8 & 9: Full Interactive Menu Loop & User Input...")
    # Simulate user inputs:
    # 1: view all
    # 2: view delayed
    # 3: view cancelled
    # 4: search flight SK142
    # 4: search non-existent flight ZZ999
    # 5: view statistics
    # 6: view operations report
    # 7: view gates
    # 99: invalid option (tests error recovery)
    # 8: quit (tests clean break)
    test_inputs = [
        "1",
        "2",
        "3",
        "4",
        "sk142",  # test case-insensitivity
        "4",
        "ZZ999",  # test not found
        "5",
        "6",
        "7",
        "99",     # invalid choice
        "8",      # exit
    ]
    
    stdin_backup = sys.stdin
    stdout_backup = sys.stdout
    sys.stdin = io.StringIO("\n".join(test_inputs) + "\n")
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    try:
        main.main_menu()
    finally:
        sys.stdin = stdin_backup
        sys.stdout = stdout_backup
        
    out = captured_output.getvalue()
    assert "ALL SCHEDULED DEPARTURES" in out
    assert "DELAYED FLIGHTS" in out
    assert "CANCELLED FLIGHTS" in out
    assert "Flight Details Found:" in out
    assert "Flight Number : SK142" in out
    assert "Flight not found: 'ZZ999'" in out
    assert "FLIGHT STATISTICS OVERVIEW" in out
    assert "AIRPORT OPERATIONS REPORT" in out
    assert "AIRPORT GATE OVERVIEW" in out
    assert "[ERROR] Invalid choice '99'" in out
    assert "Thank you for using the Airport Departure System. Goodbye!" in out
    print("  [PASS] Interactive menu handled all options, error conditions, and quit cleanly.")

if __name__ == "__main__":
    print("=" * 60)
    print("STARTING TEST SUITE")
    print("=" * 60)
    test_flight_data_integrity()
    test_flight_status_classification()
    test_statistics_calculations()
    test_gate_generation()
    test_interactive_menu_flow()
    print("\n" + "=" * 60)
    print("ALL TESTS PASSED SUCCESSFULLY! (100% PASS RATE)")
    print("=" * 60)
