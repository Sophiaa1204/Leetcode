# Fixed Length Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = 0
        window_total = 0
        res = -float('inf')

        # right = left + k - 1
        # right - left + 1 = k
        while right < len(nums):
            window_total += nums[right]
            
            while left < right and right - left + 1 > k:
                window_total -= nums[left]
                left += 1
            
            if right - left + 1 == k:
                res = max(res,window_total/k)
            right += 1
            
        return res   