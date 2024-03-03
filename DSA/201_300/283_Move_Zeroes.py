# Two Pointers - slow, fast
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        fast = 0

        while fast < len(nums):
            if nums[fast] == 0:
                fast += 1
            else:
                nums[slow],nums[fast] = nums[fast],nums[slow]
                slow += 1
                fast += 1
        
        return nums