#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

input()
set1 = set(map(int, input().split()))
input()
set2 = set(map(int, input().split()))
l1 = sorted(set1.symmetric_difference(set2))
[print(z) for z in l1]
