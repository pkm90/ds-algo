class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        
        # check the values match
        # some indice condition <= k
        
#         k = 2
#         [1,2,3,1,2,3, ....... N]
#            l r
        
        # setup window
        # k = k + 1
        k = min(len(nums), k)
        window = set()
        for i in range(k):
            window.add(nums[i])
        print(window)
        
        # if len(window) < k:
        #     return True
        
        # iterate window
        left = 0
        right = k
        while right < len(nums):
            # print(window, nums[left], nums[right],left, right)
            # print(right - left, k)
            if len(window) < k:
                print(window, left, right)
                return True   
            
            # print(window, left, right)
            window.add(nums[right])
            window.remove(nums[left])

            left += 1
            right += 1
            
            # if len(window) < (right - left):
            
        if len(window) < k:
            print(window, left, right)
            return True   
        print(window)
        return False
        
#         left = 0
#         for right in range(len(nums)): 
#             if abs(left - right) > k:
#                 continue
#                 if (nums[left] == nums[right]):
#                         # print(nums[i], nums[j], i, j, k)
#                         return True
#                 right += 1
            
        return False
