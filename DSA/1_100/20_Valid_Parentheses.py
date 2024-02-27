# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def generator(self, input):
        if input == '(':
            return ')'
        if input == '[':
            return ']'
        if input == '{':
            return '}'

    def isValid(self, s: str) -> bool:
        length = len(s)
        stack = []

        for i in range(length):
            if s[i] in ['(',"[","{"]:
                stack.append(self.generator(s[i]))
            else:
                if len(stack) != 0 and stack[-1] == s[i]:
                    stack.pop()
                else:
                    return False
            
        return len(stack) == 0