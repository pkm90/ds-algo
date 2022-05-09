# do again, took way longer than expected

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        
        
        
        
        
        # choices = {'a': a, 'b': b, 'c': c}
        
        path = ['dummy', 'dummy']
        maxHeap = [[-a, 'a'], [-b, 'b'], [-c, 'c']]
        heapq.heapify(maxHeap)
        
        while maxHeap:
            # print(maxHeap)
            count, char = heapq.heappop(maxHeap)
            # print(count, char)
            if count >= 0:
                continue
                
            # if we already used curr, then use mid
            if path[-1] == char and path[-2] == char:
                if not maxHeap:
                    break
                count2, char2 = heapq.heappop(maxHeap)
                if count2 >= 0:
                    heapq.heappush(maxHeap, [count, char])
                    continue
                count2 += 1
                path.append(char2)
                heapq.heappush(maxHeap, [count2, char2])
            else:
                count += 1
                path.append(char)
            heapq.heappush(maxHeap, [count, char])
                
        return ''.join(path[2:])
    
