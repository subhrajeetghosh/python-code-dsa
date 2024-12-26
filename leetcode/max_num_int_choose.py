from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)
        resultCount = 0
        currentSum = 0
        index = 1
        while index <= n and currentSum + index <= maxSum:
            if index not in banned_set:
                currentSum += index
                resultCount += 1
            index += 1
        return resultCount
    
    def maxCount_2nd(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_sorted = sorted(banned)
        result_count = 0
        for i in range(1, n+1):
            if(self.binery_search(banned_sorted, i)):
                continue
            maxSum -= i
            if maxSum < 0:
                break
            result_count += 1
        return result_count


    def binery_search(self, banned: List[int], target: int) -> bool:
        left = 0
        right = len(banned) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target == banned[mid]:
                return True
            elif target > banned[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return False