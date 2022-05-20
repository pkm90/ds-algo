class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        
        
        # sliding window, continuously remove min cost between consecutive duplicates
        # used pop to remove elements, but took too long so using 2 ptr now
        
        res = 0
        colors = list(colors)
        prev, i = 0, 1
        while i < len(colors):
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
            