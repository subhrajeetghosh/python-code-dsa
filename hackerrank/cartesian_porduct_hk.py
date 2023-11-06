#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

p1 = sorted(list(map(int, input().split(" "))))
p2 = sorted(list(map(int, input().split(" "))))
for i in range(len(p1)):
    current_p1 = p1[i]
    for j in range(len(p2)):
        print((current_p1, p2[j]), end=" ")
