#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

# if statement is a block of code which will execute the condition inside it's true

age = int(input("How old are you? : "))

if age == 100:
    print("Congratualtions!! you made century!! on your age")
elif age >= 18:  # this is else-if statement 
    print("you are an adult")
elif age < 0:
    print("the age is not valid")
else:  # this is default value if others are not executing then this code block will trigerred
    print("you are a child")
