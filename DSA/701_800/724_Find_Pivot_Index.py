# Prefix Sum
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        prev_sum = 0

        for i in range(0,len(nums)):
            if i >= 1:
                prev_sum += nums[i-1]
            if prev_sum == (nums_sum - nums[i]) / 2:
                return i
        
        return -1
            
