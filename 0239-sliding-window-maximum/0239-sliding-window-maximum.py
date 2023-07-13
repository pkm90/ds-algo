class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:


        
        
        
        # watched neetcode and coded this :(
        
        res = []
        l, r = 0, 0
        window = collections.deque()

        # iterate until right gets to the end of input list
        while r < len(nums):
            
            # keep popping while largest are oob
            while window and window[0][0] < l:
                window.popleft()
                
            # keep popping while the smallest is larger than current
            # this maintains a monotomically decreasing stack
            while window and window[-1][1] < nums[r]:
                window.pop()
                
            window.append([r, nums[r]])
                        
            # iterate, create window first before appending
            if r >= k - 1:
                res.append(window[0][1])
                l += 1
            r += 1
        return res
    
    
        
        # need to use a data structure to keep track track of window sorting
        # since finding next largest is an expensive operation
        # either a heap or monotomic stack...but probabl monotomic stack since heaps
        # can't keep track of when elements are added
        
        # time is n * k, since we are iterating over each element up to k times
        # space is n
                
        res = []
        l, r = 0, k
        window = Counter(nums[l:r])
        largest = max(window)
        res.append(largest)

        # iterate until right gets to the end of input list
        while r < len(nums):
            # add right
            if nums[r] not in window:
                window[nums[r]] = 1
            else:
                window[nums[r]] += 1

            # remove left
            window[nums[l]] -= 1
            if window[nums[l]] == 0:
                del window[nums[l]]
            if largest == nums[l]: # and nums[l] not in window:, this helps a bit but not enough
                largest = max(window)
            
            # iterate
            l += 1
            r += 1
            largest = max(largest, nums[r - 1])
            res.append(largest)

        return res

    
    
    
    

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # previous submissions:
    #################
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
    
    ########################################
    
        # the correct solution would be to use a deque
        # let the deque hold the valid/applicable elements, it will be monotomically decreasing/increasing
        # it removes any elements that we don't care about, aka only keeps max of the window
        #  this way, we don't have to redo old comparisons...if we the next max is larger than current max
        #  then we remove all elements and only keep that max
        # one issue is that we have to know when to remove an element and keep track of max size of deque
        # the deque keeps track of indices to easily check whether a number is in bounds
        
        res = []
        window = collections.deque()
        l, r = 0, 0
        
        while r < len(nums):
            while window and nums[window[-1]] < nums[r]:
                window.pop()
            window.append(r)
            
            # removes left if it is out of bounds
            if l > window[0]:
                window.popleft()
                
            # only start iterating left when we reach window size
            if r >= k - 1:
                res.append(nums[window[0]])
                l += 1
            r += 1

        return res
        
    ################ 
        
        # iterate until right side of window is oob
        # keep track of the window size and iterate by 1
        # append the max of everything in the window
        # this works, but run into tle
        # o(n * k) since we go over each element, up to k times
        # space: o(n - k) since we only have our result
        
        if len(nums) <= k:
            return [max(nums)]
        left, right = 0, k
        res = []
        while right < len(nums) + 1: # since window size is [inclusive: exclusive], [0:3] will indexes 0 to 2
            res.append(max(nums[left:right]))
            left += 1
            right += 1
            
        return res
    
    
