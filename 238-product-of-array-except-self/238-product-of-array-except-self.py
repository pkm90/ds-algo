# this is a bullshit problem, but very common and can help other problems
# try drawing out problem and doing it by hand to see what we need
# keep doing it...

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        
        
        res = []
        total = 1
        for curr in nums:
            res.append(total)
            total *= curr
        
        total = 1
        for curr in range(len(nums) - 1, -1, -1):
            res[curr] = res[curr] * total
            total *= nums[curr]
        
        return res
        
#         pref = []
#         post = []
#         res = []
#         total = 1
        
#         for curr in nums:
#             pref.append(total)
#             total *= curr
            
#         total = 1
#         for curr in range(len(nums) - 1, -1, -1):
#             post.append(total)
#             total *= nums[curr]
#         post.reverse()
        
#         for i in range(len(nums)):
#             res.append(pref[i] * post[i])
        
#         return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        ##################
        
        
#         pre, post = [], []
#         total = 1
#         for num in nums:
#             pre.append(total)
#             total *= num
#             # post.append(total)
#         # post.reverse()
        
#         total = 1
#         for i in range(len(nums) -1, -1, -1):
#             post.append(total)
#             total *= nums[i]
#         post.reverse()
            
            
#         res = []
#         for l, r in zip(pre, post):
#             res.append(l * r)
            
#         print(pre)
#         print(post)
#         print(res)
#         return res
        
        
        
######################33
        
        
        
#         # bruteforce is to literally go through each element except for i and calculate it
#         # we can use prefix and postfix to calculate this,
#         # prefix is everything before i, and postfix is everything after i
#         # the res = prefix[i] * postfix[i]
        
#         pre, post = [], []
        
#         total = 1
#         for i in range(len(nums)):
#             pre.append(total)
#             total *= nums[i]
            
#         total = 1
#         for i in range(len(nums) - 1, -1, -1):
#             post.append(total)
#             total *= nums[i]
#         post.reverse()

#         for i in range(len(nums)):
#             nums[i] = pre[i] * post[i]
        
#         return nums
        
        
###########################  
        
        
#         # this works, but probalby not the solution they're looking for
#         # time: n? is this n?, adding elements to hashmap would be n, and hten we iterate over each
#         #  num and go through each element in the hashmap...but lookups in hashmap is 1, so I think this is n...
#         # space: n, since we create the hashmap
#         res = []
#         storage = Counter(nums)
#         print(storage)
        
#         for num in nums:
#             storage[num] -= 1
#             total = 1
#             for key in storage:
#                 if storage[key] == 0:
#                     continue
#                 total *= key ** storage[key]
#             storage[num] += 1
#             res.append(total)
#         return res
    
    
####################

#         # optimal solution is to get prefix/postfix arrays and multiply them
#         # time: n
#         # space: n
#         # example
#         # input:   1    2   3    4
#         # prefix:  -    1   12   123
#         # postfix: 234  34  4    - 
#         # output:  234  134 124  123
#         # output:  24   12  8    6
#         prefix = [1, ]
#         postfix = [1, ]
#         n = len(nums)
#         res = []
        
#         temp = 1
#         for i in range(n):
#             temp *= nums[i]
#             prefix.append(temp)
            
#         temp = 1
#         for i in range(n-1, 0, -1):
#             # print(i)
#             temp *= nums[i]
#             postfix.insert(0, temp)
        
#         # print(prefix)
#         # print(postfix)
        
#         for i in range(len(nums)):
#             total = prefix[i] * postfix[i]
#             res.append(total)
            
#         return res