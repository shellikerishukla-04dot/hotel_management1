from hotel_management1 import bill

def test_standard_room():
    assert calculate_bill("Standard", 2) == 2000

def test_deluxe_room():
    assert calculate_bill("Deluxe", 3) == 6000

def test_suite_room():
    assert calculate_bill("Suite", 1) == 3000
