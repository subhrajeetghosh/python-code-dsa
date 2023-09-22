#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

def greet(**kwargs):
    """Greets the user by name and age.

    Args:
      **kwargs: A dictionary of keyword arguments.

    Returns:
      A greeting string.
    """

    greeting = f"Hello, {kwargs['name']}! You are {kwargs['age']} years old."
    return greeting


# Example usage:

print(greet(name="Alice", age=25))
