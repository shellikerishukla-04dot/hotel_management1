# hotel_management1.py
import sys

def calculate_bill(room, nights):
    nights = int(nights)
    if room == "Standard":
        return 1000 * nights
    elif room == "Deluxe":
        return 2000 * nights
    else:
        return 3000 * nights


# Only run this part when script is called directly
if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "Ram"
    room = sys.argv[2] if len(sys.argv) > 2 else "Standard"
    nights = sys.argv[3] if len(sys.argv) > 3 else "1"

    bill = calculate_bill(room, nights)

    print("name =", name)
    print("room =", room)
    print("bill =", bill)
