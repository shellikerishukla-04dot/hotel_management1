def calculate_bill(room_type, nights):
    prices = {
        "standard": 2000,
        "deluxe": 3500,
        "suite": 5000
    }

    if room_type not in prices:
        return None

    return prices[room_type] * nights


def main():
    print("=== Hotel Room Booking and Billing System ===")

    guest_name = input("Enter guest name: ")
    room_type = input("Enter room type (standard/deluxe/suite): ").lower()
    nights = int(input("Enter number of nights: "))

    bill_amount = calculate_bill(room_type, nights)

    if bill_amount is None:
        print("Invalid room type selected.")
        return

    print("\n--- Booking Details ---")
    print(f"Guest Name : {guest_name}")
    print(f"Room Type  : {room_type.capitalize()}")
    print(f"Nights     : {nights}")
    print(f"Total Bill : ₹{bill_amount}")


if __name__ == "__main__":
    main()
