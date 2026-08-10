class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for t in tokens:
            if t == "+" or t == "*" or t == "-" or t == "/":
                r = stack.pop()
                l = stack.pop()
                res = self.handle(t, int(l), int(r))
                stack.append(res)
            else:
                stack.append(t)
        
        return int(stack[0])
    
    def handle(self, t, l, r):
        if t == "+":
            return l + r
        elif t == "-":
            return l - r
        elif t == "*":
            return l * r
        else:
            return l / r

