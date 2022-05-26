class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        
        
        # count the elements
        # add the items into a heap
        # grab the items
        # clean the items
        # return results
        count = Counter(nums)
        maxHeap = []
        for key, count in count.items():
            maxHeap.append((-count, key))
        
        heapq.heapify(maxHeap)
        res = heapq.nsmallest(k, maxHeap)
        for i in range(len(res)):
            res[i] = res[i][1]
        return res
        
        
        
        
        
        
        
        
        
        
        # initial thoughts
        # we can put them into a heap where each element contains the number and frequency
        # then we can pop the k number of nodes
        # from an array, we would have to go through the array once and keep track of the frequencies
        # perhaps we can use a hashmap where the frequency is the key? but then how would we add to a frequency?
        #  if we use a hashmap where the key is the value, then we can add frequencies easily, but cannot search for highest k
        # or we can do above, and then create the heap from the hashmap and then pop the k most frequent
#         import heapq
#         heap = []
#         count = {}
#         res = []
        
#         for i in nums:
#             count[i] = 1 + count.get(i, 0)
#             # if i not in count:
#             #     count[i] = 0
#             # count[i] = count[i]+1
        
#         for i, j in count.items():
#             heap.append([-j, i])
#             # heap.append([j, i])
        
#         heapq.heapify(heap)
#         for i in range(k):
#             res.append(heapq.nsmallest(1, heap)[0][1])
#             heapq.heappop(heap)
#         return res
       # return [element[1] for element in heapq.nlargest(k, heap)]
        
        
        # neetcode: bucket sort (kinda)
        # create a list where the index is hte number of occurences and value is a list of numbers
        # the list will be as long as the len(inputlist)
        # if we only want k, then we simply count the returns starting from the end of list
        # go through array, keep track of counts using hashmap
        # use hashmap to insert the elements inside of the frequencyarray, index is count
        # go through the frequencyarray and append elements to resultlist
        # return the first/last k elements in resultlist
        
#         count = Counter(nums)
#         pq = []
#         for key in count:
#             pq.append([-1 * count[key], key])
            
#         heapq.heapify(pq)
#         res = heapq.nsmallest(k, pq)
#         res = [i[1] for i in res]
#         return res