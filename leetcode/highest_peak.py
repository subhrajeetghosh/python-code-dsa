from collections import deque
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows, cols = len(isWater), len(isWater[0])
        result = [[0] * cols for _ in range(rows)]
        visited = [[False] * cols for _ in range(rows)]
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if isWater[i][j] == 1:
                    result[i][j] = 0
                    visited[i][j] = True
                    queue.append((i, j))
        
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            x, y = queue.popleft()

            for dx, dy in direction:
                new_x, new_y = dx + x, dy + y
                if 0 <= new_x < rows and 0 <= new_y < cols and not visited[new_x][new_y]:
                    result[new_x][new_y] = 1 + result[x][y]
                    visited[new_x][new_y] = True
                    queue.append((new_x, new_y))
        return result