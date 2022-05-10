class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        
        
        
        
        # 1055
        # k numbers that add up to n
        # only numbers 1 through 9 are used
        # each number is used at most once
        
        # base cases
        # if path > k or total > n: return
        # if total == n: append(path) return
        # backtracking
        # we can either take the current number, or try adding without current number
        
        # we can recursively find all combinations while moving forward so we have no duplicates
        # if the total of our choices in any path == n and len(path) == k, then append and return
        
        choices = [1,2,3,4,5,6,7,8,9]
        path = []
        res = []
        
        def findCombo(idx, total):            
            if len(path) > k or total > n:
                return
            if total == n and len(path) == k:
                res.append(path.copy())
                return

            for i in range(idx + 1, 10): # choices[idx: ]: 
                path.append(i)
                findCombo(i, total + i)
                path.pop()            
        
        findCombo(0, 0)
        return res
        
        