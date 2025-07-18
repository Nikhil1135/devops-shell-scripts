import sys

# Check if there are any arguments passed
if len(sys.argv) > 1:
    print("Command-line arguments received:")
    for i, arg in enumerate(sys.argv[1:], start=1):  # Skip the first one (script name)
        print(f"Arg {i}: {arg}")
else:
    print(" No command-line arguments passed.")
