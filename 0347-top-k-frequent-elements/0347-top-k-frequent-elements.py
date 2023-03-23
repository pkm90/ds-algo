class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        
        
#         # count elements, put into array where idx is the freq
#         count = Counter(nums)
#         freq = [ [] for i in range(len(nums)) ]
#         print(count)
#         for key, cnt in count.items():
#             freq[cnt - 1].append(key)
#         print(freq)
        
#         # iterate backwards until result hold k elements
#         res = []
#         for i in range(len(freq) - 1, -1, -1):
#             for num in freq[i]:
#                 res.append(num)
#                 if len(res) == k:
#                     return res
#         print('outside')
        
        
        
        
        
        res = []
        count = {}
        # hashmap = {key : val} {num : count}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
            
            
        print(count)
        
        # iterate through counts, keep track of top, return top
        
        temp = []
        for key,val in count.items():
            temp.append([val,key])

        
        # time complexity of sorting: nlogn
        temp.sort(reverse = True)
        print(temp)
        
        for i in range(k):
            res.append(temp[i][1])
            
        print(res)
        return res
        
        
        
        
        
        