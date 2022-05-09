class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        
        
        
        
        
        
        
        
        
        
        # backtrack through all combinations and return result
        # time: N since we only hit each element once, 
        # space: N for recursion stack, path, and res
        
        # have to check if input is none, base case would break
        # have to check if input is empty string, would return a list with empty string
        # works for all valid inputs, 2-9
        
        def createCombo(idx):
            # base
            if idx >= len(digits):
                res.append(''.join(path))
                return
            
            # try each letter of the current choices
            for letter in choices[digits[idx]]:
                path.append(letter)
                createCombo(idx + 1)
                path.pop()
                
        # check input            
        if len(digits) == 0:
            return []
        
        # variables
        choices = {'2': ['a','b','c'],
                  '3': ['d','e','f',],
                  '4': ['g','h','i',],
                  '5': ['j','k','l',],
                  '6': ['m','n','o',],
                  '7': ['p','q','r','s',],
                  '8': ['t','u','v',],
                  '9': ['w','x','y','z',]}  
        path = []
        res = []
        
        # create combinations
        createCombo(0)
        
        # return result
        return res
        
        
        #####################################
        
        
#         if len(digits) is 0: return None
        
#         # build choices as a list of lists
#         digits = list(digits) # so that we can slice easier
#         letters = {'2': ['a','b','c'],
#                   '3': ['d','e','f',],
#                   '4': ['g','h','i',],
#                   '5': ['j','k','l',],
#                   '6': ['m','n','o',],
#                   '7': ['p','q','r','s',],
#                   '8': ['t','u','v',],
#                   '9': ['w','x','y','z',]}
#         path = []
#         combo = []        
        
    
#         # base: if len(path) == len(digits), then append and return
#         # process: go through all potential paths and recursively call function
#         #  add to the path and remove afterwards    
#         def combination(choices):
#             if len(choices) == 0:
#                 temp = ''.join(path)
#                 combo.append(temp)
#                 return
            
#             for letter in letters[choices[0]]:
#                 path.append(letter)
#                 combination(choices[1:])
#                 path.pop()
        
#         combination(digits)
#         print(combo)
#         return combo
        
        

        