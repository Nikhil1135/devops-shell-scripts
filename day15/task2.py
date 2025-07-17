class NegativeNumberError(Exception):
    pass

def check_positive(num):
    if num < 0:
        raise NegativeNumberError("Negative numbers not allowed.")

try:
    number = int(input("Enter a positive number: "))
    check_positive(number)
    print("Great! You entered:", number)
except NegativeNumberError as e:
    print(e)
except ValueError:
    print("Please enter a valid number.")
