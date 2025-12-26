import sys

# Safe argument handling
name = sys.argv[1] if len(sys.argv) > 1 else "Unknown"
room = sys.argv[2] if len(sys.argv) > 2 else "Standard"
nights = int(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[3].isdigit() else 1

# Calculate bill
if room == "Standard":
    bill = 1000 * nights
elif room == "Deluxe":
    bill = 2000 * nights
else:
    bill = 3000 * nights

print("name =", name)
print("room =", room)
print("bill =", bill)
