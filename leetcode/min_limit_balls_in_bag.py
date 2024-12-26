#https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag
from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right = 1, max(nums)
        result = right
        while left < right:
            mid = left + (right - left) // 2
            if self.isPossibleWithCurrentBall(nums, maxOperations, mid):
                result = mid
                right = mid
            else:
                left = mid + 1
        return result

    def isPossibleWithCurrentBall(self, nums: List[int], maxOperation: int, currentBall: int):
        currentOperation = 0
        for i in nums:
            currentOperation += (i - 1) // currentBall
            if currentOperation > maxOperation:
                return False
        return True
