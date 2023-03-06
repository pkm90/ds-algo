class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        
        
        
        # [0,3,7,1,2,5,8,4,6,0, -1]
        # {0: 17,
        #  3: 1,
        #  7: 1,
        #  2: 2,
        #  1: 17}
        
        # if current num is 1
        # check if 0 or 2 have already been visited
        
        # o(1) lookups in hashset are o(1)
        # looking up +1 -1
        
        numSet = set(nums)
        visit = set()
        
        res = 0
        
        for num in numSet:
            counter = 1
            curr = num
            
            # skip if visited
            if num in visit:
                continue
            
            # go through entire consecutive group
            while curr - 1 in numSet:
                counter += 1
                visit.add(curr)
                curr -= 1
                
            curr = num
            while curr + 1 in numSet:
                counter += 1
                visit.add(curr)
                curr += 1
            
            res = max(res, counter)
            
        return res
            
            
            
                
#             # add key if it doesn't exist
#             if num not in seen:
#                 seen[num] = 1
            
#             # check if +1 -1 exists
#             # update their values
#             while curr + 1 in seen:
#             if num + 1 in seen:
#                 seen[num] = seen[num] + seen[num + 1]
#             if num - 1 in seen:
#                 seen[num] = seen[num] + seen[num - 1]
            
#             if num + 1 in seen:
#                 seen[num + 1] = seen[num]
#             if num - 1 in seen:
#                 seen[num - 1] = seen[num]
            
#             res = max(res, seen[num])
        
#         print(seen)
            
#         return res
            
                
        
        
        