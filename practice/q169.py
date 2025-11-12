from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def getMajority(left,right):
            if left == right:
                return nums[left]
            mid = left + (right-left) //2
            left_majority = getMajority(left,mid)
            right_majority = getMajority(mid+1,right)

            if left_majority == right_majority:
                return left_majority
            
            left_count = sum(1 for i in range(left,right+1) if nums[i]==left_majority)
            right_count = sum (1 for i in range(left,right+1) if nums[i]==right_majority)

            return left_majority if left_count > right_count else right_majority
        return getMajority(0,len(nums)-1)


# Example usage:
solution = Solution()
nums = [3,2,3]
print(solution.majorityElement(nums))  # Output: 3
