class Solution:
    def findDuplicate(self, nums):
        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
# test
s = Solution()
print(s.findDuplicate([1,3,4,2,2]))  # Output: 2
