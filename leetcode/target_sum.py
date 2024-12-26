class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.findWays(nums, target, -1, 0)
    
    def findWays(self, nums: List[int], target: int, index: int, sum: int) -> int:
        if index == len(nums):
            return 1 if target == sum else 0
        add = self.findWays(nums, target, index+1, sum + nums[index])
        substract = self.findWays(nums, target, index+1, sum - nums[index])
        return add + substract