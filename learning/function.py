#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

# function is a block of code which is executed when it is only called

def hello():
    print("Hello, World!")


hello()


def add_two_numbers(a, b):
    """Returns the sum of two numbers.

    Args:
      a: A number.
      b: A number.

    Returns:
      The sum of a and b.
    """

    return a + b  # return statment python values/objects back to the caller


print(add_two_numbers(12, 43))
