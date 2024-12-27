class Solution:
    def findTargetSumWays_2nd(self, nums: List[int], target: int) -> int:
        return self.findWays(nums, target, -1, 0)
    
    def findWays(self, nums: List[int], target: int, index: int, sum: int) -> int:
        if index == len(nums):
            return 1 if target == sum else 0
        add = self.findWays(nums, target, index+1, sum + nums[index])
        substract = self.findWays(nums, target, index+1, sum - nums[index])
        return add + substract
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.memo = {}
        self.findWays_2(nums, target, -1, 0)

    def findWays_2(self, nums: List[int], target: int, index: int, sum: int) -> int:
            key = sum + " " + index
            if key in self.memo:
                 return self.memo[key]
            index += 1
            if index == len(nums):
                 return 1 if target == sum else 0
            add = self.findWays_2(nums, target, index, sum + nums[index])
            substract = self.findWays_2(nums, target, index, sum - nums[index])

            self.memo[key] = add + substract
            return self.memo[key]
    
    