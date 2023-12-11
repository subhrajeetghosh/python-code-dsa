#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

def add(*stuff):  # you can define any name but * is must
    total_sum = 0
    for i in stuff:
        total_sum += i

    return total_sum


print(add(1, 2, 3, 4, 5, 6, 7))


def example_function_with_parameter(param1, *args):
    print("Parameter 1:", param1)
    for arg in args:
        print(arg)


# Calling the function with different numbers of arguments
example_function_with_parameter('first', 1, 2, 3)
example_function_with_parameter('second', 'a', 'b', 'c', 'd')
example_function_with_parameter('third')