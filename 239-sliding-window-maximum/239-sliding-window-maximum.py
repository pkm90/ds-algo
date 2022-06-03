class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        ###############
        res = []
        l, r = 0, k - 1
        stack = collections.deque() # [index, val]
        for i in range(k):
            while stack and stack[-1][1] < nums[i]:
                stack.pop()
            stack.append([i, nums[i]])
        res.append(stack[0][1])
        print(stack)
        
        for r in range(k, len(nums), 1):
            while stack and stack[0][0] <= r - k:
                stack.popleft()
            while stack and stack[-1][1] < nums[r]:
                stack.pop()
            stack.append([r, nums[r]])
            res.append(stack[0][1])
            
        return res