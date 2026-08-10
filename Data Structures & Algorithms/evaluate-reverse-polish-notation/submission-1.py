class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for t in tokens:
            if not self.is_operator(t):
                stack.append(t)
            else:
                r = stack.pop()
                l = stack.pop()
                res = self.handle(t, int(l), int(r))
                stack.append(res)
        
        return int(stack[0])

    
    def is_operator(self, n):
        if n == "+" or n == "*" or n == "-" or n == "/":
            return True
        return False
    
    def handle(self, t, l, r):
        if t == "+":
            return l + r
        elif t == "-":
            return l - r
        elif t == "*":
            return l * r
        else:
            return l / r

