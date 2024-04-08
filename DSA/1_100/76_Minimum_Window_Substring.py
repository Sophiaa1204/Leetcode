# Non-fixed Sliding Window

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        # [left, right)
        dict_s = collections.defaultdict(int)
        dict_t = collections.defaultdict(int)
        left = 0
        right = 0
        start = 0
        length = float("inf")
        matc = 0
        need = 0

        for c in t:
            if dict_t[c] == 0:
                need += 1
            dict_t[c] += 1
        
        while right < len(s):
            dict_s[s[right]] += 1
            if dict_s[s[right]] == dict_t[s[right]]:
                matc += 1
            right += 1

            while left < right and matc == need:
                if length > right - left:
                    start = left
                    length = right - left
                if dict_s[s[left]] == dict_t[s[left]]:
                    matc -= 1
                dict_s[s[left]] -= 1
                left += 1
        
        # length = right - left
        # start = right - length
        # print(start,length)
        if length == float('inf'):
            return ""
        else:
            return s[start:(start+length)]