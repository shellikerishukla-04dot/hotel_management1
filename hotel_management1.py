import sys

def main():
    # Expecting 3 arguments: guest_name, room_type, nights
    if len(sys.argv) != 4:
        print("Usage: python hotel_management.py <guest_name> <room_type> <nights>")
        print("Example: python hotel_management.py Alice Deluxe 3")
        return

    guest_name = sys.argv[1]
    room_type = sys.argv[2]
    try:
        nights = int(sys.argv[3])
    except ValueError:
        print("Error: Nights must be a number.")
        return

    # Room prices
    room_prices = {
        "Standard": 1000,
        "Deluxe": 2000,
        "Suite": 3000
    }

    # Check if room type is valid
    if room_type not in room_prices:
        print(f"Invalid room type! Choose one of: {', '.join(room_prices.keys())}")
        return

    cost_per_night = room_prices[room_type]
    total_bill = cost_per_night * nights

    print("=== Hotel Room Booking and Billing System ===")
    print(f"Guest Name    : {guest_name}")
    print(f"Room Type     : {room_type}")
    print(f"Nights Stayed : {nights}")
    print(f"Cost per Night: ₹{cost_per_night}")
    print(f"Total Bill    : ₹{total_bill}")

if __name__ == "__main__":
    main()
