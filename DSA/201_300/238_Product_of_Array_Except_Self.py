class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = 0
        res = [0 for _ in range(len(nums))]

        for num in nums:
            if num == 0:
                zeros += 1
            else:
                product *= num
        
        if zeros == 0:
            for i in range(len(nums)):
                res[i] = product // nums[i]
        
        if zeros == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    res[i] = product

        return res