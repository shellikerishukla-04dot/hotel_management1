import sys

# Check if enough arguments provided
if len(sys.argv) < 4:
    print("Error: please provide name, room and nights")

    sys.exit()

name = sys.argv[1]
room = sys.argv[2]
nights = int(sys.argv[3])

# simple bill calculation
if room == "Standard":
    bill = 1000 * nights
elif room == "Deluxe":
    bill = 2000 * nights
else:
    bill = 3000 * nights

print("name =", name)
print("room =", room)
print("bill =", bill)
