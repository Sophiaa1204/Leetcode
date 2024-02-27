# Dictionary
# Time Complexity: O(len(s)+len(t))
# Space Complexity: O(26) -> 26 characters
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        collection = dict()
        # Build the collection
        for i in range(len(s)):
            if s[i] in collection:
                collection[s[i]] += 1
            else:
                collection[s[i]] = 1
        # Check
        for i in range(len(t)):
            if t[i] not in collection:
                return False
            else:
                collection[t[i]] -= 1
                if collection[t[i]] < 0:
                    return False
        
        return True