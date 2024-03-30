# Backtrack - Subsets
class Solution:
    def __init__(self):
        self.track = []
        self.res = []
    
    def backtrack(self,nums,start):
        self.res.append(self.track[:])

        for i in range(start,len(nums)):
            self.track.append(nums[i])
            self.backtrack(nums,i+1)
            self.track.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums,0)
        return self.res
   