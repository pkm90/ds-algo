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
        current = 0
        
        path = []
        res = []
        visit = set()
        
        def findCombo(idx, total):
            # print(idx, total, path)
            # if (idx, total) in visit:
            #     return
            # visit.add((idx, total))
            
            if total == n and len(path) == k:
                res.append(path.copy())
                return
            if len(path) > k or total > n or idx == 10:
                return

                
            
            for i in choices[idx: ]:  # take try taking these numbers
                path.append(i)
                findCombo(i, total + i)
                path.pop()
            
            # findCombo(idx + 1, total)     # try not taking any numbers and moving to next
            
        
        findCombo(0, 0)
        return res
        
        