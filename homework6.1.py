#Get string from user
from enum import unique

user_input = input("Do you have any cars?")

#Convert string into a set - duplicate are automatically removed
unique_chairs = set(user_input)

#countunique char
unique_count = len(unique_chairs)

#check if more than 10 unique char
if unique_count > 10:
    print(True)
    else:
    print(False)