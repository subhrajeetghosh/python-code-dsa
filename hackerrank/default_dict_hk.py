#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

from collections import defaultdict

d = defaultdict(list)


def intialize_dict(size, index_name):
    for _ in range(size):
        current_word = input()
        d[index_name].append(current_word)


n, m = map(int, input().split())
intialize_dict(n, "A")
intialize_dict(m, "B")

for word in d["B"]:
    if word in d["A"]:
        indices = []
        for index, value in enumerate(d["A"]):
            if value == word:
                indices.append(index + 1)
        print(" ".join(map(str, indices)))
    else:
        print("-1")
