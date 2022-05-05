class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # pretty simple, main thing to watch out for is how
        # the elements are ordered and how to truncate towards 0
        # for negative numbers it's different, easiest way is to
        # conv to int
        stack = []
        for token in tokens:
            if token == "+":
                r, l = stack.pop(), stack.pop()
                stack.append(l + r)
            elif token == "-":
                r, l = stack.pop(), stack.pop()
                stack.append(l - r)
            elif token == "*":
                r, l = stack.pop(), stack.pop()
                stack.append(l * r)
            elif token == "/":
                r, l = stack.pop(), stack.pop()
                stack.append(int(l / r))
            else:
                stack.append(int(token))
        return stack[0]