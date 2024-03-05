# Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0,len(nums)-1
        res = [0] * len(nums)
        res_pointer = len(nums) - 1

        while left <= right:
            left_square = nums[left] * nums[left]
            right_square = nums[right] * nums[right]

            if left_square < right_square:
                res[res_pointer] = right_square
                right -= 1
            else:
                res[res_pointer] = left_square
                left += 1
            
            res_pointer -= 1
        
        return res