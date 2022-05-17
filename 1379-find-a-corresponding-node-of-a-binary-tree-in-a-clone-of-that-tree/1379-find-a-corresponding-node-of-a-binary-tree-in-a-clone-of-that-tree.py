class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        # iterate through both trees at once, if original.curr == target then return cloned.curr
        
        
        def dfs(normal, cloned):
            if normal is None:
                return None
            if normal == target:
                return cloned
            
            lnode = dfs(normal.left, cloned.left)
            rnode = dfs(normal.right, cloned.right)
            return lnode or rnode
        
        return dfs(original, cloned)
        
        
        
        
        
        q = collections.deque()
        q.append((original, cloned)) # each element is a node from original and cloned
        
        while q:
            normalCurr, clonedCurr = q.popleft()
            
            if normalCurr == target:
                return clonedCurr
            if normalCurr.left:
                q.append((normalCurr.left, clonedCurr.left)) # traversing through both trees at same time
            if normalCurr.right:
                q.append((normalCurr.right, clonedCurr.right))