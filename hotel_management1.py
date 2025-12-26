import sys

# Check argument count
if len(sys.argv) != 4:
    print("Usage: python hotel_management.py <guest_name> <room_type> <nights>")
    sys.exit()

guest_name = sys.argv[1]
room_type = sys.argv[2]
nights = int(sys.argv[3])

# Decide price using if-else
if room_type == "Standard":
    price = 1000
elif room_type == "Deluxe":
    price = 2000
elif room_type == "Suite":
    price = 3000
else:
    print("Invalid room type")
    sys.exit()

total = price * nights

print("=== Hotel Billing System ===")
print("Guest Name:", guest_name)
print("Room Type:", room_type)
print("Nights:", nights)
print("Total Bill: ₹", total)
