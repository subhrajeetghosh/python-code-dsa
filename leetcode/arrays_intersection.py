#  Copyright (c) 2024.
#  @Author Subhrajeet Ghosh
from typing import List


def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    set_array1 = set(nums1)
    set_array2 = set(nums2)
    set_result = set_array1.intersection(set_array2)
    return list(set_result)


def intersection_part2(self, nums1: List[int], nums2: List[int]) -> List[int]:
    set_array = set()
    for num in nums1:
        set_array.add(num)
    set_result = set()
    for num in nums2:
        if num in set_array:
            set_result.add(num)
    return list(set_result)
