class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [0] + digits
        digits[len(digits)-1] += 1

        for i in range(len(digits)-1,0,-1):
            if digits[i] != 10:
                break
            else:
                digits[i] = 0
                digits[i-1] += 1
        
        if digits[0] == 0:
            return digits[1:]
        else:
            return digits[:]