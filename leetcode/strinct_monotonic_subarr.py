class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        strictIn, strictDc, maxIn, maxDc = 1, 1, 1, 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                strictIn += 1
                maxIn = max(strictIn, maxIn)
            else:
                strictIn = 1
            if nums[i] > nums[i+1]:
                strictDc += 1
                maxDc = max(strictDc, maxDc)
            else:
                strictDc = 1
        return max(maxIn, maxDc)