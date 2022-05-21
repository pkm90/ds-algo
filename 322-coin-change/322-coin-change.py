class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # checked my solution, not sure if I can do it quickly -.-
        # bfs since we're finding min number of coins
        # can memoize based on amount since any amount is the min number of coins to reach
        q = collections.deque()
        q.append([0, 0]) # numCoins, total value of coins
        visit = set()
        
        while q:
            numCoins, total = q.popleft()
            if total > amount:
                continue
            if total in visit:
                continue
            visit.add(total)
            
            if total == amount:
                return numCoins
            
            for coin in coins:
                q.append((numCoins + 1, total + coin))
        
        return -1
        
        
        
        
        
        
#         # time limit exceeded, adding memo
#         def dfs(goal, level, minimum):
#             # if level > minimum:
#             #     return
#             if goal <= 0:
#                 if goal == 0:
#                     # print('found')
#                     minimum = min(minimum, level)
#                     memo[goal] = minimum
#                     return memo[goal]
#                 else:
#                     return
#             if goal in memo:
#                 return memo[goal]
            
#             for coin in coins: # in range(1, len(coins)):
#                 if goal - coin >= 0:
#                     print(coin)
#                     memo[goal] = dfs(goal-coin, level+1, minimum)
#                     print('memo', memo)
                    
#                 # mincoins = min(dfs(goal - coins[coin], level + 1), dfs(goal - coins[coin-1], level + 1))
#                 # memo[goal] = mincoins
#             return memo[goal]
#         # minimum = 0
#         memo = {}
#         dfs(amount, 0, float(inf))
#         print(memo)
#         return memo[11] if memo[11] else -1
                
#         memo = {}
#         res = []
#         dfs(amount, 0)
#         return min(res) if len(res)>0 else -1
        
    
    
#         # a bit upset since I couldn't get the true dp solution, and couldn't memoize it
#         # but found a solution from looking at a few bfs solutions to get ideas:
# def coinChange2(self, coins: List[int], amount: int) -> int:
#         """
#         Use BFS which is to find the shortest path from 0 to amount.
#         This is much faster than the above dp solution.
#         """
#         if not amount:  # Don't need any coin.
#             return 0

#         queue = deque([(0, 0)])
#         visited = [True] + [False] * amount
#         while queue:
#             totalCoins, currVal = queue.popleft()
#             totalCoins += 1  # Take a new coin.
#             for coin in coins:
#                 nextVal = currVal + coin
#                 if nextVal == amount:  # Find a combination.
#                     return totalCoins

#                 if nextVal < amount:  # Could add more coins.
#                     if not visited[nextVal]:  # Current value not checked.
#                         visited[nextVal] = True  # Prevent checking again.
#                         queue.append((totalCoins, nextVal))

#         return -1  # Cannot find any combination.
    
        # we move backwards from the amount we are trying to reach
        # since this is bfs, we will always find the shortest path
        # the key is to refrain from going down the same path multiple times
        # so we use the visited set. If we have already been through trying out coins
        # for the amount we are currently on, then we skip it
#         q = collections.deque([(amount, 0)]) # total, level
#         visited = set()
#         while q:
#             curr, level = q.popleft()
#             if curr == 0:
#                  return level
#             if (curr in visited or curr < 0):
#                 continue
#             visited.add(curr)

#             for coin in coins:
#                 if curr - coin >= 0:
#                     q.append((curr-coin, level+1))
#         print(visited)
#         return -1
    
    
################################################################################################
        # 03/23/2022
        # coins, amount
        # 9:51
        # finished iterative solution quickly, recursive took way too long
        # return smallest number of coins to match amount, can use unlimited coins
        # it's kind of like what is the shortest path, except the vertices aren't as clear
        # for example coins = [1,2,5] and amount = 11
        # we can always take paths 1, 2, 5
        # when we reach our goal, then we can keep track of min number of coins needed to get here
        # we can do this iteratively or recursively, but I think iteratively would make more sense
        # since we are looking to minimize the path and bfs would do this
        
        # used hashmap, better to use visited set instead
        # time: n * amount, since we are potentially storing that many inside memo
        # space: n * amount, same as above
#         q = collections.deque([(0, 0)]) # total, coins
#         memo = {}
        
#         while q:
#             # print(q)
#             currTotal, numCoins = q.popleft()
#             # print(currTotal, numCoins)
#             if currTotal == amount:
#                 # print(memo)
#                 return numCoins
#             elif currTotal > amount:
#                 continue
#             if currTotal in memo:
#                 continue
#             else:
#                 memo[currTotal] = numCoins
            
#             for coin in coins:
#                 q.append((currTotal + coin, numCoins + 1))
#         return -1
    
    
    
    
    
    
    
    
    
    
    
    
    
        # recursive
        # this took forever to get working -.-
        # this works, but hits time limit
        # checked if memo works and it does but still hit time limits
        # not a good solution, try again in future
#         memo = {}
#         def backtrack(total, numCoins):
#             if total == amount:
#                 # print(total, numCoins)
#                 memo[total] = min(memo.get(total, float(inf)), numCoins)
#                 return memo[total]
#             if (total in memo and memo[total] <= numCoins):
#                 print('time saved')
#                 return memo[total]
#                 # memo[total] = min(memo[total], numCoins)
#                 return memo[total]
                        
#             for coin in coins:
#                 if total + coin <= amount:
#                     # print(total, numCoins, coin)
#                     levels = backtrack(total + coin, numCoins + 1)
#                     # print('before', memo)
#                     memo[total] =  min(memo.get(total, float(inf)), levels)
#                     # print(memo)
#             return memo.get(total, -1)# if memo[total] is None else -1
        
#         backtrack(0, 0)
#         print(memo)
#         return memo[amount] if amount in memo.keys() else -1
        