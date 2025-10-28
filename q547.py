from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find(x) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
        
        cities = len(isConnected)
        parent = list(range(cities))
        
        for i in range(cities):
            for j in range(i + 1, cities):
                if isConnected[i][j] == 1:
                    union(i, j)
        
        provinces = sum(parent[i] == i for i in range(cities))
        return provinces
# 测试
if __name__ == "__main__":
    solution = Solution()
    isConnected = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 1]
    ]
    print(solution.findCircleNum(isConnected))  # 输出: 2
    