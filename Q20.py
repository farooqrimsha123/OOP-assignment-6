# 20. Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this
#  exception if age < 18. Handle it with try...except.


# Custom exception class

class InvalidAgeError(Exception):
    def __init__(self , message):
        self.message = message


def check_age(age):
    try:
        if age < 18:
            raise InvalidAgeError("Invalid age: Age must be 18 or older.")
        else:
            print("Age is valid.")
    except InvalidAgeError as e:
        print(e.message)



check_age(15)  # Output: Invalid age: Age must be 18 or older.
check_age(20)  # Output: Valid age.

        