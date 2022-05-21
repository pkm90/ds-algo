# perpetual problem, strings practice

class Solution:
    def decodeString(self, s: str) -> str:
        
        
        
        
        
        
        
        # I have to go through the string backwards
        # unblock the last codes, use the output to unblock last - 1 codes
        # when there are no more codes, we are finished
        
        
        stack = []        
        for char in s:     # continue until we reach the end of the string
            if char != "]":       # append items to a stack if it's not closing bracket
                stack.append(char)
            else:                 # closing bracket found, find the string and number, append to stack
                tempStr = []
                tempNum = []
                while stack and stack[-1].isalpha():
                    tempStr.append(stack.pop())
                tempStr.reverse()
                tempStr = ''.join(tempStr)
                
                stack.pop() # remove the open bracket
                
                while stack and stack[-1].isdigit():
                    tempNum.append(stack.pop())
                tempNum.reverse()
                tempNum = int(''.join(tempNum))
                
                stack.append(tempStr * tempNum)
        
        return ''.join(stack)
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #################################
        
        # this is considered a difficult problem, lots of comments saying it should be a hard
        # the only hard part about this problem is the nested brackets
        # whenever we find a problem(brackets), we have to solve the subproblems(nested brackets)
        # this can be done recursively, or with a stack
        
        # loop through and add each char to a stack
        # if we find a closing bracket
        #  then we grab the internal string
        #  then we find the number preceding the bracket
        #  then we append the internalstring*number to the stack
        # if we find another closing bracket, then the internal problem is solved and the repeat is accurate
        # finally, by the end of the initial loop (adding each char to stack), the stack is in the desired order
        # we can return it as a string using the join function
        
#         result = ''
#         stack = []
#         for i in s:
#             if i == ']':
#                 # find internal string
#                 # pop characters until we find an opening bracket
#                 inside_string = ''
#                 while stack and stack[-1]!='[':
#                     temp = stack.pop()
#                     inside_string = temp+inside_string
#                 stack.pop() # for the opening bracket
                                
#                 # find int
#                 inside_int = ''
#                 while stack and stack[-1].isdigit():
#                     temp = stack.pop()
#                     inside_int = temp + inside_int
#                 inside_int = int(inside_int)
                
#                 # add entire string*int to the stack
#                 stack.append(inside_int*inside_string)
#             else:
#                 stack.append(i)
                
#         result = result.join(stack)
#         return result
        
        
        
        