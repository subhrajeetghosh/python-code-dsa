#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

# Keyword arguments in Python are a way to pass arguments to a function by name. This can be useful for making code
# more readable and maintainable

def hello(first, middle, last):
    print(first + " " + middle + " " + last)


hello("1st", "2nd", "3rd")

hello(last="1st", middle="3rd", first="2nd")
