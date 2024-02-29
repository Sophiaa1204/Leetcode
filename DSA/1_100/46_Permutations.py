# Backtrack
# Time Complexity: O(N!)
class Solution:
    def __init__(self):
        self.res = []
    
    def backtrack(self,track,choices,nums):
        if len(track) == len(nums):
            self.res.append(track.copy())
            return
        
        for i in range(len(nums)):
            if choices[i]:
                continue

            choices[i] = True
            track.append(nums[i])
            self.backtrack(track,choices,nums)
            track.pop()
            choices[i] = False


    def permute(self, nums: List[int]) -> List[List[int]]:
       track = []
       choices = [False] * len(nums)

       self.backtrack(track,choices,nums)

       return self.res