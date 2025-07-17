try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
except ZeroDivisionError:
    print(" Cannot divide by zero!")
except ValueError:
    print(" Invalid input. Please enter a number.")
else:
    print(f" Division successful! Result: {result}")
finally:
    print(" This block always runs (cleanup, logging, etc).")
