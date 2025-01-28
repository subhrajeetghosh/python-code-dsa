from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    result = max(result, self.dfs(grid, i, j))
        return result

    def dfs(self, grid: List[List[int]], i: int, j: int) -> int:
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            return 0
        ans = grid[i][j]
        grid[i][j] = 0
        ans += self.dfs(grid, i+1, j)
        ans += self.dfs(grid, i-1, j)
        ans += self.dfs(grid, i, j+1)
        ans += self.dfs(grid, i, j-1)
        return ans