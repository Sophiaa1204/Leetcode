# Two Pointers: slow - fast
# Time Complexity: O(n)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        fast = 1

        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow],nums[fast] = nums[fast], nums[slow]
            fast += 1
        
        return slow + 1