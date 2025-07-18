from datetime import datetime, timedelta

# Get the current date and time
now = datetime.now()
print("📅 Current Date and Time:", now)

# Format the date/time output
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("⏱️ Formatted Date and Time:", formatted)

# Show yesterday and tomorrow
yesterday = now - timedelta(days=1)
tomorrow = now + timedelta(days=1)

print("⬅️ Yesterday:", yesterday.strftime("%A, %d %B %Y"))
print("➡️ Tomorrow:", tomorrow.strftime("%A, %d %B %Y"))
