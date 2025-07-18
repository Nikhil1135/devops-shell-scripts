import os

# Step 1: Check if 'logs' folder exists
if not os.path.exists("logs"):
    os.mkdir("logs")
    print(" 'logs' folder created.")
else:
    print(" 'logs' folder already exists.")

# Step 2: Create 'today.txt' inside 'logs'
file_path = os.path.join("logs", "today.txt")

# Step 3: Create the file (or overwrite if it exists)
with open(file_path, "w") as f:
    f.write("")  # Writing nothing creates an empty file
    print("📄 'today.txt' file created inside 'logs'.")
