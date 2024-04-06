# Binary Search
# 1、返回的这个值是 nums 中大于等于 target 的最小元素索引。

# 2、返回的这个值是 target 应该插入在 nums 中的索引位置。

# 3、返回的这个值是 nums 中小于 target 的元素个数。
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        # left = right + 1
        return left