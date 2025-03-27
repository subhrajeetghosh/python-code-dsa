#  Copyright (c) 2025.
#  @Author Subhrajeet Ghosh
from collections import Counter


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        totalFreq = Counter(nums)
        dominant = None
        for key in totalFreq:
            if totalFreq[key] > len(nums) // 2:
                dominant = key
                break
        leftCounter = 0
        for i in range(len(nums)):
            if nums[i] == dominant:
                leftCounter += 1
            leftLength = i + 1
            if leftLength // 2 < leftCounter and (len(nums) - leftLength) // 2 < totalFreq[dominant] - leftCounter:
                return i
        return -1
