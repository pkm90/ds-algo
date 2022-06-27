class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
         # hashmap
        visited = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in visited:
                return (visited[diff], i)
            visited[num] = i
        
        popularity = [1,2,3]
        k = 3
        print('f',sum([]))
        scores = []
        path = []

        def dfs(idx):
            if idx >= len(popularity):
                tempScore = sum(path)
                if (len(scores) >= k and tempScore > scores[0]):
                    heapq.heappop(scores)
                    heapq.heappush(scores, tempScore)
                    # return
                elif len(scores) < k:
                    heapq.heappush(scores, tempScore)
                return

            # we can take the item
            path.append(popularity[idx])
            dfs(idx + 1)
            path.pop()

            # we can choose not to take the item
            dfs(idx + 1)
        
        # find combos
        dfs(0)
        
        # sort the combinations
        print(scores)
        scores.sort()
        res = scores[-k:]
        res.sort(reverse = True)
        
        print(res)
        print('done')
        # return the top k scores
        return res


        temp.sort()
        print(temp)
        return
        # arr = ["eo", 
        #         "09z", 
        #         "az0", 
        #         "236"]
        # arr.sort()
        # print(arr)
        # return
        
        boxList = [["first qpx", "eo"], 
                ["cat hamster", "09z"], 
                ["first qpx", "az0"], 
                ["cat dog rabbit snake", "236"]]
        
        boxList = ["ykc 82 01", 
                "eo first qpx", 
                "09z cat hamster", 
                "06f 12 25 6", 
                "az0 first qpx", 
                "236 cat dog rabbit snake"]
        # arr.sort()
        # print(arr)
        # return
        old, new, res = [], [], []
        splitBox = []
        for box in boxList:
            # print(box)
            splitBox.append(box.split(" "))

        # print(splitBox)
        for box in splitBox:
            if box[1].isalpha():
                old.append(box)
            else:
                new.append(box)

        # modify old boxes so that versioning comes first, and then identifier
        # this way the sorting will sort by the versioning first and then identifier
        temp = []
        for i, box in enumerate(old):
            tempString = []
            for section in box[1:]:
                tempString.append(section + " ")
            tempString[-1] = tempString[-1][:-1] # removes trailing space
            tempString = [''.join(tempString)]
            tempString.append(box[0])
            temp.append(tempString)

        heapq.heapify(temp)
        old = []
        while temp:
            box = heapq.heappop(temp)
            tempString = [box[1]," ", box[0]] # swap positions of identifier and versioning to original
            tempString = ''.join(tempString)
            old.append([tempString])
        
        for i, box in enumerate(old):
            res.append(box[0])
            
        for i, box in enumerate(new):
            temp = []
            for b in box:
                temp.append(b + " ")
            temp[-1] = temp[-1][:-1]
            res.append(''.join(temp))
        print(len(res))
        print(res)
        return res
        print('old', old)
        # extend and return
        res.extend(old)
        res.extend(new)
        print(res)
        return res












        
        arr = ["ykc 82 01", 
                "eo first qpx", 
                "09z cat hamster", 
                "06f 12 25 6", 
                "az0 first qpx", 
                "236 cat dog rabbit snake"]
        # print(arr)
        
        test = {}
        test = []
        
        # arr.split(" ")
        
        splitBox = []
        for box in arr:
            splitBox.append(box.split(" "))

        # for box in splitBox:
        #     if box[1].isalpha():
        #         old.append(box)
        #     else:
        #         new.append(box)
            
        temp = []
        for i, box in enumerate(splitBox):
            box
            tempString = []
            for section in box[1:]:
                tempString.append(section + " ")
            tempString[-1] = tempString[-1][:-1] # removes trailing space
            tempString = [''.join(tempString)]
            tempString.append(box[0])
            temp.append(tempString)
            # print(temp)
        
        heapq.heapify(temp)
        old = []
        res = []
        while temp:
            box = heapq.heappop(temp)
            tempString = [box[1], " ", box[0]]
            tempString = ''.join(tempString)
            old.append(tempString)
        print(old)
        return
        
        while temp:
            old.append(heapq.heappop(temp))
            # print(heapq.heappop(temp))
        res.extend(old)
        # res.extend(new)
        for i in res:
            print(i)
        return
        
        
        for box in arr:
            box = box.split(" ")
            temp = []
            for section in box[1:]:
                temp.append(section + " ")
            box = [box[0]]
            box.append(''.join(temp))
            # box[1] = [box[1:]]
            print(box)
            if box[1][1].isalpha():
                test.append(box)
                
            # test.append(box.split(" "))
            # print(box)
            
        print(test)
        heapq.heapify(test)
        print(test)
        
        
        
        
        # # bruteforce
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums), 1):
        #         if nums[i] + nums[j] == target:
        #             return (i, j)
                
#         # hashmap
#         visited = {}
#         for i, num in enumerate(nums):
#             diff = target - num
#             if diff in visited:
#                 return (visited[diff], i)
#             visited[num] = i
            
        # bruteforce, 2ptrs and sort, hashmap
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return[i, j]
        
        
        # prevMap = {}
        # for i, num in enumerate(nums):
        #     diff = target - num
        #     if diff in prevMap:
        #         return[i, prevMap[diff]]
        #     prevMap[num] = i
                
#         # 2 ptrs
#         # not sure if this is gonna work, can't sort it
#         # we can sort it, but have to keep track of original indexes which is hassle
#         # time: nlogn
#         # space: 1
        
#         l, r = 0, len(nums)-1
#         sorted(nums)
#         while l < r:
#             total = nums[l] + nums[r]
#             if total == target:
#                 return [l, r]
#             if total > target:
#                 l += 1
#             else:
#                 r -= 1
#         return None
        
        # # hashmap
        # # time: n
        # # space: n
        # memo = {}
        # for i, num1 in enumerate(nums):
        #     num2 = target - num1
        #     if num2 in memo:
        #         return [memo[num2], i]
        #     memo[num1] = i