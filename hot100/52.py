from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        
        # 初始化队列和新鲜橘子数量
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        if fresh_count == 0:
            return 0  # 没有新鲜橘子
        
        minutes = 0
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        # BFS 扩散腐烂
        while queue and fresh_count > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr, nc))
            minutes += 1
        
        return minutes if fresh_count == 0 else -1

# Example usage:
sol = Solution()
grid = [
    [2,1,1],
    [1,1,0],
    [0,1,1]
]
print(sol.orangesRotting(grid))  # Output: 4