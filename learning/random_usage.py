#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

import random

x = random.randint(1, 99)
print(x)

myList = ["hello", "hi", "hey"]
print(random.choice(myList))

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random.shuffle(nums)
print(nums)
