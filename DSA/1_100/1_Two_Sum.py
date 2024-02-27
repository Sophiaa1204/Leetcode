# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i in range(len(nums)):
            desire = target - nums[i]
            if desire in num_dict.keys():
                return [num_dict[desire],i]
            else:
                num_dict[nums[i]] = i