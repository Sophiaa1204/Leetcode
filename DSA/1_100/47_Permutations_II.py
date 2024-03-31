# Backtrack - Permutations with Repeatation
class Solution:
    def __init__(self):
        self.res = []
        self.track = []
        self.used = []

    def backtrack(self,nums):
        if len(self.track) == len(nums):
            self.res.append(self.track.copy())
            return
        
        for i in range(len(nums)):
            if self.used[i]:
                continue
            if i > 0 and nums[i] == nums[i-1] and not self.used[i-1]:
                continue
            
            self.track.append(nums[i])
            self.used[i] = True
            self.backtrack(nums)
            self.track.pop()
            self.used[i] = False

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.used = [False] * len(nums)
        nums.sort()
        self.backtrack(nums)
        return self.res