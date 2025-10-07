from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashtable = set()
        for num in nums:
            if num in hashtable:
                return True
            hashtable.add(num) 
        return False
# 测试
if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3,1]
    print(solution.containsDuplicate(nums))  # 输出 True
    nums = [1,2,3,4]
    print(solution.containsDuplicate(nums))  # 输出 False