from hotel_management1 import bill

def test_standard_room():
    assert bill("Standard", 2) == 2000

def test_deluxe_room():
    assert bill("Deluxe", 3) == 6000

def test_suite_room():
    assert bill("Suite", 1) == 3000
