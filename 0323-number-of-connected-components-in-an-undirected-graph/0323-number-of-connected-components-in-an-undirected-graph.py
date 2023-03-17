class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
          
        
#         adj = {node: [connections]}
#         adj = {0: [1],
#                1: [0, 2],
#                2: [1],
#                3: [4],
#                4: [3]}
        
#         captains = [0,1,2,3,4]
#         people = [1,1,1,1,1]        
        
        
#         for i in in:
#             captain.append([i, 1])
            
#         for node, others in adj.items():
            
#         for edge in edges:
#             left = edge[0]
#             right = edge[1]
            
#         if people[left] > people[right]:
#             captain[right] = captain[left]
#         else:
#             captain[left] = captain[right]
        
            
        
        
        
            
        captain = { i:i for i in range(n) }
        army = { i:1 for i in range(n) }
        print(captain)
        print(army)
        
        # if root is itself, return it
        # otherwise, recursively set root to it's parent
        def find(n):
            if captain[n] == n:
                return n
            captain[n] = find(captain[n])
            return captain[n]
            
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return
            if army[p1] >= army[p2]:
                captain[p2] = p1
                army[p1] += army[p2]
            else:
                captain[p1] = p2
                army[p2] += army[p1]
                
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

        