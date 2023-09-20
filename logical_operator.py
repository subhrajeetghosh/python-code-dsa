#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

# logical operator (and, or, not) = used to check if two or more conditional checks
temperature = int(input("What's the temperature? :"))

if 16 <= temperature <= 30:
    print("temperature is normal today")
elif temperature <= 15 and temperature % 2 == 0:  # and is for adding statement in condition
    print("temperature is coll and even!!")

if not (16 <= temperature <= 30):  # if not is a reverse statement of if
    print("temperature is not normal today")
