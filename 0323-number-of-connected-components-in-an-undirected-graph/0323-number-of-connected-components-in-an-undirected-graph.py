class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
            
        # captain = { i:i for i in range(n) }
        captain = {}
        for i in range(n):
            captain[i] = i
        
        army = { i:1 for i in range(n) }
        print("captains: ", captain)
        print("army:     ", army)
        
        # if root is itself, return it
        # otherwise, recursively set root to it's parent
        def find(n):
            if captain[n] == n:
                return n
            captain[n] = find(captain[n])
            return captain[n]
        
        # find returns the captain of a group
            
        def union(n1, n2):
            left, right = find(n1), find(n2)
            if left == right:
                return
            
            if army[left] >= army[right]:
                captain[right] = left
                army[left] += army[right]
            else:
                captain[left] = right
                army[right] += army[left]
                
                
        # edges.sort()
        # print(edges)
        for edge in edges:
            union(edge[0], edge[1])
        
        for node in range(n):
            find(node)
        
        print('--------------')
        print(captain)
        print(army)
        captains = captain.values()
        numCaptains = set(captains)
        return len(numCaptains)

        