class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #################
        
        
        # add open if possible, check num open to input
        # add closed if possible, check num closed to num open
        
        def dfs(numOpen, numClosed):
            if numClosed == n:
                res.append(''.join(path))
                
            if numOpen < n:
                path.append("(")
                dfs(numOpen + 1, numClosed)
                path.pop()
            
            if numClosed < numOpen:
                path.append(")")
                dfs(numOpen, numClosed + 1)
                path.pop()
        
        path = []
        res = []
        dfs(0, 0)
        return res