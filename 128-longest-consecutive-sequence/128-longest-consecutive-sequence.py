# do again

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        
        
        
        
#         nums = set(nums)
#         choices = set()
#         longest = 0
        
#         for num in nums:
#             streak = 1
#             if num - 1 not in nums:
#                 while num + 1 in nums: # and num not in choices:
#                     streak += 1
#                     num += 1
#                     # choices.add(num)
#                 longest = max(longest, streak)
            
#         return longest
        
        def findLongest(num):
            if num not in nums:
                return
            if num in visited:
                return
            visited.add(num)
            streak[0] += 1
            # longest[0] = max(longest[0], streak[0])
            
            if num + 1 in nums:
                findLongest(num + 1)
            if num - 1 in nums:
                findLongest(num - 1)
            
        nums = set(nums)
        visited = set()
        longest = 0
        for num in nums:
            if num not in visited:
                streak = [0]
                findLongest(num)
                longest = max(longest, streak[0])
        
        return longest
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    ##############################
        
#         # the bruteforce solutions are actually really simple and well written
#         # I'm going to start practicing the bruteforce solutions so I can practice coding them
#         # below is bruteforce
#         maxStreak = 0
#         for num in nums:
#             streak = 1
#             while num + 1 in nums:
#                 num = num + 1
#                 streak += 1
#             maxStreak = max(maxStreak, streak)
#         return maxStreak
        
        # we can use a hashmap to optimize the above bruteforce
        # store each number and instead of looking inside the input nums, we can check the key of hashmap
        # to optimize, we only want to check if a previous number does NOT exist
        #  if it does exist, then we know that it won't make a new streak
#         maxStreak = 0
#         numSet = set(nums)
#         for num in nums:
#             numSet.add(num)
#             streak = 1
#             if num - 1 not in numSet:
#                 while num + 1 in numSet:
#                     num += 1
#                     streak += 1
#                 maxStreak = max(maxStreak, streak)
#         # print(numSet)
#         return maxStreak
        
    #########################33
    
    # looking at my below solution after a few weeks
    # shit I'm so damn smart... not sure if I can do this during interviews
    
        # if we say that elements are connected if their difference is 1
        # then we can do a unionfind and grab the max that have the same element
        # we have an array of integers, how will we set up the edges?
        # for each element, add it to a set and see if +-1 exists
        #  if it exists, then add that edge to the unionfind
        # time: linear since find just returns it's parent (although worst case is that it will go through n times once)
        #       union calls find twice and commpares ranks, all constant/linear operations
        #       the actual code to go through and make the edges/unions iterates through and checks +-1
        # space: linear, worst case we will have roots and ranks which scale by n for each of them
        
        
#         if nums is None or len(nums) is 0: return 0
#         # setting up unionfind, have to use hashmap since input isn't same as index
#         roots = { i:i for i in nums }
#         ranks = { i:1 for i in nums }
        
#         # if root is itself, return it
#         # otherwise, recursively set root to it's parent
#         def find(n):
#             if roots[n] == n:
#                 return n
#             roots[n] = find(roots[n])
#             return roots[n]
            
#         def union(n1, n2):
#             p1, p2 = find(n1), find(n2)
#             if p1 == p2:
#                 return
#             if ranks[p1] >= ranks[p2]:
#                 roots[p2] = p1
#                 ranks[p1] += ranks[p2]
#             else:
#                 roots[p1] = p2
#                 ranks[p2] += ranks[p1]
                
#         for i in nums:
#             if i + 1 in roots:
#                 union(i, i + 1)
#             if i - 1 in roots:
#                 union(i, i - 1)
        
#         return max(ranks.values())