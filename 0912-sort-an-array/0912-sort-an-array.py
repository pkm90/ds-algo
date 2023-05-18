class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # base
        if len(nums) <= 1:
            return nums
        
        # find middle
        mid = len(nums)//2
        
        # print(nums, mid)
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        
        # print('left, right', left, right)
        
        res = self.mergeLists(left, right)
        return res
    
    def mergeLists(self, l1, l2):
        p1, p2 = 0, 0
        res = []
        # print('merging', l1, l2)
        while (p1 < len(l1) and p2 < len(l2)):
            if l1[p1] < l2[p2]:
                res.append(l1[p1])
                p1 += 1
            else:
                res.append(l2[p2])
                p2 += 1
            
        if p1 < len(l1):
            res.extend(l1[p1:])
        if p2 < len(l2):
            res.extend(l2[p2:])
        return res