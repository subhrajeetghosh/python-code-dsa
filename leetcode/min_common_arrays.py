#  Copyright (c) 2024.
#  @Author Subhrajeet Ghosh
from typing import List


# link - https://leetcode.com/problems/minimum-common-value/
def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            return nums2[j]
        if nums1[i] > nums2[j]:
            j += 1
        else:
            i += 1
    return -1
