# ✅ Day 17 – Python: Loops Recap, Lists & Dictionaries, datetime & sys.argv

## 📚 Topics Covered

- Python `for` loops
- Python `while` loops
- Lists: indexing, looping, and operations
- Dictionaries: key-value pairs, iteration
- `datetime` module
  - Getting the current date and time
  - Formatting dates
- `sys.argv`
  - Command-line argument handling

## 🧠 What You Learned

- How to use `for` and `while` loops with lists and dictionaries.
- Accessing elements of a list and dictionary using indexing and keys.
- Using Python's built-in `datetime` module to fetch and format timestamps.
- Using `sys.argv` to pass arguments via the command line and how to parse them.

## 🧪 Tasks Practiced

1. Looping through a list of DevOps tools using:
   - `for item in list`
   - `for i in range(len(list))`
   - `while` loop

2. Dictionary iteration:
   - Printed tool names and their descriptions using `.items()`.

3. Used `datetime.now()` to display current date and time.

4. Used `sys.argv` to write a script that greets the user by name passed from the command line.

## 🛠️ Mini-Project (Weekend Task Reminder)

Build a script that accepts a name and a date via `sys.argv`, checks if the date is today's date using `datetime`, and prints a message accordingly:
- If the date is today, print: `"Hello <name>, today is the day!"`
- Else, print: `"Hello <name>, your event is not today!"`

## 📌 Notes

- Always check `len(sys.argv)` before accessing arguments to avoid index errors.
- Use `datetime.strptime()` to convert a string to a `datetime` object for comparisons.
