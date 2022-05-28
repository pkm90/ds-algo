# really good tricks and techniques, keep doing this problem
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        
        # count elements, put into array where idx is the freq
        count = Counter(nums)
        freq = [ [] for i in range(len(nums)) ]
        for key, cnt in count.items():
            freq[cnt - 1].append(key)
        print(freq)
        
        # iterate backwards until result hold k elements
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        print('outside')
                
        
        
        
#         # count elements, put in hashmap
#         count = Counter(nums)
        
#         # throw elements into heap
#         heap = [ (-1 * freq, key) for key, freq in count.items() ]
#         heapq.heapify(heap)
        
#         # pop from heap k times
#         res = []
#         # res = heapq.nsmallest(k, heap)
#         # res = [ key for freq, key in res ]
#         for i in range(k):
#             curr = heapq.heappop(heap)
#             res.append(curr[1])
#         return res
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #############################3
        
#         n = len(nums)
#         ordered = [ [] for _ in range(n + 1) ]
#         res = []
        
#         count = Counter(nums)
        
#         for key, num in count.items():
#             ordered[num].append(key)
#         ordered.reverse()
        
#         for numSet in ordered:
#             for num in numSet:
#                 res.append(num)
#                 if len(res) == k:
#                     return res
        
        #######################
        
        
#         # bucketsort, kinda...
#         # really good trick, keep doing this problem
#         count = Counter(nums)
#         freq = [ [] for i in range(len(nums) + 1) ]
#         for key, cnt in count.items():
#             freq[cnt].append(key)
#         print(freq)
        
#         res = []
#         for i in range(len(freq) -1, -1, -1):
#             res.extend(freq[i])
        
#         return res[:k]
        
        
        # count the elements
        # add the items into a heap
        # grab the items
        # clean the items
        # return results
#         count = Counter(nums)
#         maxHeap = []
#         for key, count in count.items():
#             maxHeap.append((-count, key))
        
#         heapq.heapify(maxHeap)
#         res = heapq.nsmallest(k, maxHeap)
#         for i in range(len(res)):
#             res[i] = res[i][1]
#         return res
        
        
        ###################3
        
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