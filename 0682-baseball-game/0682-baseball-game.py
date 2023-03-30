class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        
        # use stack to keep track of record
        # do operation
        def operation(op):
            if op == '+': 
                return stack[-1] + stack[-2]
            if op == 'D': 
                return stack[-1] * 2
            # isnumeric and isdigit don't work with negative
            # if it gets to this case, it's definitely an int
            # just cast and return
            # if op.isnumeric():
            return int(op)
            
        stack = []
        res = 0
        
        for oper in operations:
            # print(oper, stack)
            if oper == 'C':
                stack.pop()
                continue
            stack.append(operation(oper))
        
        for num in stack:
            res += num
        
        
        return res