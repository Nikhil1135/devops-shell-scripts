# ✅ Day 15 – Python Exception Handling

## 📚 Topics Covered

### 1. Built-in Exception Handling
- Use of `try`, `except`, `else`, and `finally` blocks
- Handling specific exceptions like `ZeroDivisionError` and `ValueError`

### 2. Custom Exceptions
- Creating and using user-defined exceptions using Python classes
- Raising exceptions based on custom logic
- Catching custom exceptions with informative messages

---

## 🧪 Tasks

### 🔹 Task 1 – Handle Built-in Exceptions
**Goal:** Gracefully handle user input and division errors.

```python
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(num1 / num2)

except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input. Please enter a number.")
else:
    print("Division successful.")
finally:
    print("This block always runs.")


