# Binary Search

# 1、返回的这个值是 nums 中大于等于 target 的最小元素索引。

# 2、返回的这个值是 target 应该插入在 nums 中的索引位置。

# 3、返回的这个值是 nums 中小于 target 的元素个数。

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        while left <= right:
            mid = left + (right-left) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
        
        return left - 1