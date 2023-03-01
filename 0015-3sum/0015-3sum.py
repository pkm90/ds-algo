class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        
        # return all triplets that sum==0 and are unique
        
        used = set()
        res = []
        
        nums.sort()
        # print(nums)
#         [     c   l        r   ]
#         [-2, -1, -1, 0, 1, 2, 3]

        
        # if sum is < 0, iterate m
        # if sum is > 0, iterate r
        # if sum == 0,   iterate l
        
        
        for curr in range(len(nums) - 2):
            l = curr + 1
            r = len(nums) - 1
            # print(curr)
            while l < r:
                
                total = nums[curr] + nums[l] + nums[r]

                if total == 0:
                    if (nums[curr], nums[l], nums[r]) not in used:
                        # print(curr, l, r)
                        used.add((nums[curr], nums[l], nums[r]))
                        res.append([nums[curr], nums[l], nums[r]])
                    # else:
                    #     break
                if total < 0:
                    l = l + 1
                else:
                    r = r - 1
        
        # print(used)
        return res