class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        
        # True if there are duplicates within a window of size k
        
        # check edgecase where k in larger than input
        k = min(len(nums), k)
        
        # setup window
        window = set()
        for i in range(k):
            window.add(nums[i])
        print(window)
                
        # iterate window
        left = 0
        right = k
        while right < len(nums):
            # print(window, nums[left], nums[right],left, right)
            if len(window) < k:
                print("inner: ", window, left, right)
                return True   
            
            window.add(nums[right])
            window.remove(nums[left])
            left += 1
            right += 1

        # check final window
        if len(window) < k:
            print("final: ", window, left, right)
            return True
        
        print("False: ", window)
        return False
        
#         left = 0
#         for right in range(len(nums)): 
#             if abs(left - right) > k:
#                 continue
#                 if (nums[left] == nums[right]):
#                         # print(nums[i], nums[j], i, j, k)
#                         return True
#                 right += 1
            
#         return False
