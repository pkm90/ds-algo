class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        visited, cost = set(), 0
        frontier = [[0, (points[0])], ]
        heapq.heapify(frontier) 
        print(points)
        adj = { (i, j):[] for i, j in points }
        for i in range(len(points)):
            for j in range(len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[(points[i][0], points[i][1])].append((dist, points[j]))
                adj[(points[j][0], points[j][1])].append((dist, points[i]))
                
        while len(visited) != len(adj.keys()):
            # print(frontier)
            weight, x = heapq.heappop(frontier)
            # print(weight, x)
            if (x[0], x[1]) in visited:
                continue
            visited.add((x[0], x[1]))
            
            cost += weight
            for weight, nei in adj[(x[0], x[1])]:
                # calculate weights here or when initializing the adj list
                if (nei[0], nei[1]) not in visited:
                    heapq.heappush(frontier, (weight, nei))
        
        return cost
        
        
        if len(points) == 1:
            return 0
        res = 0
        visit = set()
        edgeCost = {}
        frontier = []
        
        
        adj = {}
        # point: [[cost, point], [cost, point]...]
        
        for edge0 in points:
            for edge1 in points:
                if edge0 == edge1:
                    continue
                point0 = str(edge0[0]) + str(edge0[1])
                point1 = str(edge1[0]) + str(edge1[1])
                cost = abs(edge0[0] - edge1[0]) + abs(edge0[1] - edge1[1])
                
                if point0 in edgeCost:
                    edgeCost[point0].append([cost, point1])
                else:
                    edgeCost[point0] = [[cost, point1]]
                
                if point1 in edgeCost:
                    edgeCost[point1].append([cost, point0])
                else:
                    edgeCost[point1] = [[cost, point0]]
                
        point = str(points[0][0]) + str(points[0][1])
        visit.add(point)

        for edge in edgeCost[point]:
            heappush(frontier, [edge[0], edge[1]])
        
        while len(visit) < len(edgeCost):
            curr = heappop(frontier)
            print(curr)
            while curr[1] in visit:
                curr = heappop(frontier)
            visit.add(curr[1])
            res += curr[0]
            
            for edge in edgeCost[curr[1]]:
                heappush(frontier, edge)
        
        return res
            
            
            
            
            
            
            