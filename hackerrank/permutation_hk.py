#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

from itertools import permutations

string, k = input().split(" ")
perm_list = sorted(permutations(string, int(k)))
for i in perm_list:
    print(''.join(i))
