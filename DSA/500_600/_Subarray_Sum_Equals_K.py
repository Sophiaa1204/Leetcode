# Hash Table + Prefix Sum
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_dict = {0:1}
        pre_sum = 0
        count = 0

        for num in nums:
            pre_sum += num
            if pre_sum - k in pre_dict.keys():
                count +=  pre_dict[pre_sum-k]
            if pre_sum in pre_dict.keys():
                pre_dict[pre_sum] += 1
            else:
                pre_dict[pre_sum] = 1
        
        return count