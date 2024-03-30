# Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        res = 0

        while left < right:
            curr_sum = (right-left) * min(height[left],height[right])
            res = max(curr_sum,res)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return res