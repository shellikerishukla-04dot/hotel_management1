import sys

def main():
    if len(sys.argv) > 1:
        guest_name = sys.argv[1]
    else:
        guest_name = "Unknown"
    print(f"Guest name: {guest_name}")

if __name__ == "__main__":
    main()
