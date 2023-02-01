class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # implement any sort function that sorts in place, quicksort or mergesort
        # for practice, let's try bucketsort and mergesort
        
        
        # bucketsort, if input has neg then need to figure somehting else out
        # bucketoneline = [0 for i in range(len(nums))]
        bucket = [i for i in range(max(nums) + 1)]
        for i in range(max(nums) + 1):
            bucket[i] = 0
            
        for i in nums:
            bucket[i] += 1
        
        # res = []
        pos = 0
        for i in range(len(bucket)):
            for j in range(bucket[i]):
                # res.append(i)
                nums[pos] = i
                pos += 1
                
