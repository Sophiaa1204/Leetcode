# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# Binary Search

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        # left = right + 1
        return left