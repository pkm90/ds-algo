class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        
        # use stack to keep track of record
        # do operation
        def operation(op):
            if op == '+': 
                return stack[-1] + stack[-2]
            if op == 'D': 
                # print(stack)
                return stack[-1] * 2
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