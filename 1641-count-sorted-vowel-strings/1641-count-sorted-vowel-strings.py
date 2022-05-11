class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        
        
        
        
        # 1108
        
        
        
        choices = ['a','e','i','o','u']
        # self.elements = 0
        self.res = 0
        
        def dfs(idx, elements):
            if elements == n:
                self.res += 1
                return
            if idx == len(choices):
                return
            
            for i in range(idx, len(choices)):
                dfs(i, elements + 1)
            
        dfs(0, 0)
        return self.res