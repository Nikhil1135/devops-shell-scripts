def greet_people(*args):
    for name in args:
        print(f"hello {name} !!")

def show_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")


if __name__ == "__main__":
    greet_people("Nikhil", "Gabbar", "AVU")
    show_profile(name="Nikhil", role="DevOps Engineer", location="India")

import calculator

print("Addition  : ", calculator.add(12, 23))
print("subtraction : ", calculator.subtract(45, 28)) 