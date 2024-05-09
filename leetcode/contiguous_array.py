#  Copyright (c) 2024.
#  @Author Subhrajeet Ghosh
from typing import List


def findMaxLength(self, nums: List[int]) -> int:
    sum_nums = 0
    map_dict = {0: -1}
    result = 0
    for i in range(len(nums)):
        sum_nums += -1 if nums[i] == 0 else 1
        if sum_nums in map_dict:
            result = max(result, i - map_dict[sum_nums])
        else:
            map_dict[sum_nums] = i
    return result
