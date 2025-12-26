import sys

# Get command-line arguments
name = sys.argv[1]
room = sys.argv[2]
nights = int(sys.argv[3])

# Calculate bill using if-else
if room == "Standard":
    bill = 1000 * nights
elif room == "Deluxe":
    bill = 2000 * nights
else:
    bill = 3000 * nights

print("name =", name)
print("room =", room)
print("bill =", bill)
