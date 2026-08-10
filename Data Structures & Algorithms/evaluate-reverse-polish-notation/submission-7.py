class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for t in tokens:
            if t == "+" or t == "*" or t == "-" or t == "/":
                r = int(stack.pop())
                l = int(stack.pop())
                if t == "+":
                    res = l + r
                elif t == "-":
                    res = l - r
                elif t == "*":
                    res = l * r
                else:
                    res = l / r
                stack.append(res)
            else:
                stack.append(t)
        
        return int(stack[0])

