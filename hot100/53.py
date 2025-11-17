from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import deque
        
        indegree = [0] * numCourses     # 每门课的入度
        graph = [[] for _ in range(numCourses)]  # 邻接表

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        count = 0
        while queue:
            course = queue.popleft()
            count += 1
            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        return count == numCourses

# test
sol = Solution()
numCourses = 2
prerequisites = [[1,0],[0,1]]
print(sol.canFinish(numCourses, prerequisites))  # Output: False