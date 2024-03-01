# Dictionary
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        collection = dict()

        # construct the dictionary
        for i in magazine:
            if i not in collection:
                collection[i] = 1
            else:
                collection[i] += 1

        # check
        for i in ransomNote:
            if i not in collection:
                return False
            else:
                if collection[i] == 0:
                    return False
                collection[i] -= 1
        
        return True