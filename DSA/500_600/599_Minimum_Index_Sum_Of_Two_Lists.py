class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic = dict()
        len1 = len(list1)
        len2 = len(list2)

        for i in range(len1):
            dic[list1[i]] = i
        
        min_idx = len1 + len2
        ans = []
        for j in range(len2):
            if list2[j] in dic.keys():
                sum = j + dic[list2[j]]
                if min_idx > sum:
                    min_idx = sum
                    ans = [list2[j]]
                elif min_idx == sum:
                    ans.append(list2[j])
        
        return ans