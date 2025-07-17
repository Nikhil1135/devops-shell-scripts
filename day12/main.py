from functions_demo import welcome, add_numbers, get_user_role
from file_utils import file_exists
import math
welcome()

sum_result = add_numbers(3, 7)
print(f"The sum of numbers is : {sum_result}")


experience = int(input("Enter your exp in years : "))
role = get_user_role(experience)
print(f" Based on your exp , You are a : {role}")


file = input("Enter a file name to check: ")
if file_exists(file):
    print("The file exists..")
else:
    print("The file you entered doesn't exists...")

    print(math.sqrt(49))