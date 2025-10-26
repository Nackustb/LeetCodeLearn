from typing import List
# DFS
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if grid is None:
#             return 0

#         rows, cols = len(grid), len(grid[0])
#         count = 0

#         def dfs(r, c):
#             if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
#                 return
#             grid[r][c] = '0'
#             dfs(r - 1, c)
#             dfs(r + 1, c)
#             dfs(r, c - 1)
#             dfs(r, c + 1)

#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == '1':
#                     count += 1          # 发现一个新岛屿
#                     dfs(r, c)       # 把整座岛都淹掉

#         return count


# BFS
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        def bfs(r, c):
            q = deque([(r, c)])
            grid[r][c] = '0'
            while q:
                x, y = q.popleft()
                for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '1':
                        grid[nx][ny] = '0'
                        q.append((nx, ny))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count += 1
                    bfs(i, j)

        return count


# Example usage:
solution = Solution()   
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print(solution.numIslands(grid))  # Output: 3