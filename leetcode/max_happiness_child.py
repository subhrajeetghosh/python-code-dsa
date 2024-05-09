#  Copyright (c) 2024.
#  @Author Subhrajeet Ghosh
from typing import List


def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
    current_k = k
    happiness.sort()
    result = 0
    for i in range(len(happiness) - 1, -1, -1):
        if happiness[i] - (k - current_k) < 0 or current_k < 1:
            break
        result += happiness[i] - (k - current_k)
        current_k -= 1
    return result
