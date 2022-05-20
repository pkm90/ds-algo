class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        
        
        # sliding window, continuously remove min cost between consecutive duplicates
        
        res = 0
        colors = list(colors)
        prev, i = 0, 1
        while i < len(colors):
        # for left in range(len(colors) - 1):
            print(prev, i)
            if colors[prev] == colors[i]:
                small, big = prev, i
                if neededTime[small] > neededTime[big]:
                    small, big = big, small
                res += neededTime[small]
                # neededTime.pop(small)
                # colors.pop(small)
                prev = big
            else:
                prev = i
            i += 1
        
        return res
            