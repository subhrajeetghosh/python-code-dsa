#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    elif n > 20:
        print("Not Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    else:
        print("Weird")
