# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0
        curr_count = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                curr_count += 1
            else:
                max_len = max(max_len, curr_count)
                curr_count = 0
        
        max_len = max(max_len, curr_count)
        
        return max_len