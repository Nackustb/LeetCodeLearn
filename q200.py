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
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        def bfs(r, c):
            queue = [(r, c)]
            grid[r][c] = '0'
            while queue:
                row, col = queue.pop(0)
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                        grid[nr][nc] = '0'
                        queue.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1      # 发现一个新岛屿
                    bfs(r, c)       # 把整座岛都淹掉

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