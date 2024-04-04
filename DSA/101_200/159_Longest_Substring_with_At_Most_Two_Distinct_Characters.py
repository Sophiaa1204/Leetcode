# Sliding Window

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        dic = dict()
        curr_count = 0
        res = 0
        curr_res = 0

        left = 0
        right = 0

        while right < len(s):
            if s[right] in dic.keys():
                dic[s[right]] += 1
            else:
                curr_count += 1
                dic[s[right]] = 1
            
            curr_res += 1
            
            while curr_count > 2:
                if dic[s[left]] == 1:
                    del dic[s[left]]
                    curr_count -= 1
                else:
                    dic[s[left]] -= 1
                curr_res -= 1
                left += 1
            
            res = max(res,curr_res)
            right += 1
        
        return res