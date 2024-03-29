# Using Stack
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []

        for i in tokens:
            if i not in "+-*/":
                stack.append(int(i))
            else:
                if len(stack) >= 2:
                    op1 = stack.pop()
                    op2 = stack.pop()
                    

                if i == "+":
                    ans = op2 + op1 
                    
                elif i == "-":
                    ans = op2 - op1
                
                elif i == "*":
                    ans = op2 * op1
                
                elif i == "/":
                    ans = int(op2/op1) # Note here!

                stack.append(ans)
        
        return int(stack[0])