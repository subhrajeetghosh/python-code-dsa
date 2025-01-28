from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        top = [0] * len(grid[0])
        bottom = [0] * len(grid[0])
        top[0] = grid[0][0]
        bottom[0] = grid[1][0]
        for i in range(1, len(grid[0])):
            top[i] = top[i-1] + grid[0][i]
            bottom[i] = bottom[i-1] + grid[1][i]
        result = float('inf')
        for i in range(len(grid[0])):
            top_max = top[len(grid[0])-1] - top[i]
            bottom_max = 0 if i == 0 else bottom[i-1]
            result = min(result, max(top_max, bottom_max))
        return result