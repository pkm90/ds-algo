class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        
        
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
        # add k:v to res, sort, return [:k]
        
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
        
        
        