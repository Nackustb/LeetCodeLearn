from typing import List
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i , j = 0 ,len(people)-1
        res = 0
        while i <= j :
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
            res += 1
        return res
# Example usage:
solution = Solution()
people = [3,2,2,1]
limit = 3
print(solution.numRescueBoats(people, limit))  # Output: 3
