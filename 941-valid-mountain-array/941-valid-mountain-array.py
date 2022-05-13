class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        
        i = 0 
        n = len(arr)
        up, down = False, False
        if n < 3:
            return False
        
        # walk up the mountain
        while i < n - 1 and arr[i] < arr[i + 1]:
            up = True
            i = i + 1
        
        # walk down the mountain
        while i < n - 1 and arr[i] > arr[i + 1]:
            down = True
            i = i + 1
            
        # if we didn't reach the end, then it isn't a mountain
        if i == n - 1 and up and down:
            return True
        else:
            return False
        