#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

# set which is unordered and unindexed containes no duplicates values

a = {1, 2, 3}
a.add(5)  # {1, 2, 3, 5}
a.remove(3)  # {1, 2, 5}

# two sets relations

b = {2, 3, 4}

print(a.union(b))  # {1, 2, 3, 4, 5}   add both of them
print(a.intersection(b))  # {2}  in common
print(a.difference(b))  # {1, 5} element that are not present in b compare to a
print(a.symmetric_difference(b))  # {1, 3, 4, 5}  element tat are not present in both set
a.update(b)  # a = {1, 2, 3, 4}
