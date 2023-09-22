#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

def add(*stuff):  # you can define any name but * is must
    total_sum = 0
    for i in stuff:
        total_sum += i

    return total_sum


print(add(1, 2, 3, 4, 5, 6, 7))
