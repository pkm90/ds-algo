# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# class TimeMap:

#     def __init__(self):
        

#     def set(self, key: str, value: str, timestamp: int) -> None:
        

#     def get(self, key: str, timestamp: int) -> str:

# class TimeMap:

#     def __init__(self):
        

#     def set(self, key: str, value: str, timestamp: int) -> None:
        

#     def get(self, key: str, timestamp: int) -> str:

# class TimeMap:

#     def __init__(self):
        

#     def set(self, key: str, value: str, timestamp: int) -> None:
        

#     def get(self, key: str, timestamp: int) -> str:

# class TimeMap:

#     def __init__(self):
        

#     def set(self, key: str, value: str, timestamp: int) -> None:
        

#     def get(self, key: str, timestamp: int) -> str:
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
################################

# we can use a hashmap of lists
# hashmap is the key : list
# list is [ timestamp : value ]

class TimeMap:

    def __init__(self):
        self.storage = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.storage:
            self.storage[key].append([timestamp, value])
        else:
            self.storage[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        # kinda like bruteforce, let's optimize this search by using binary search
        # prev = ""
        # for time, value in self.storage[key]:
        #     if time == timestamp:
        #         return value
        #     if time > timestamp:
        #         break
        #     prev = value
        # return prev
        
        res = ""
        values = self.storage.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            if values[mid][0] == timestamp:
                return values[mid][1]
            
            if values[mid][0] < timestamp:
                res = values[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res
        
#         if key not in self.storage:
#             return ""

#         bucket = self.storage[key]
#         l, r = 0, len(bucket) - 1
#         while l <= r:
#             mid = (l + r) // 2
#             time, value = bucket[mid]
#             if timestamp == time:
#                 return value
            
#             if timestamp < time:
#                 r = mid - 1
#             else:
#                 l = mid + 1
                
#         if bucket[r][0] < timestamp:
#             # print('right')
#             return bucket[r][1]
#         return ""        
        
        
#         # below I'm trying hte template, gave up...changed to something I understand...
#         res = ''
#         bucket = self.storage.get(key, [])
#         l, r = 0, len(bucket) - 1
#         while l <= r:
#             mid = (l + r) // 2
#             currTime, value = bucket[mid]
#             if currTime <= timestamp:
#                 res = value
#                 l = mid + 1
#             else:
#                 r = mid - 1
#         return res
        
#         print(bucket)
#         return bucket[l][1]
#         if bucket[l][0] == timestamp:
#             print('found')
#             print(timestamp, bucket[l][0])
#             return bucket[l][1]
        
#         l, r = 0, len(bucket) - 1
#         while l < r:
#             mid = (l + r) // 2
#             currTime, value = bucket[mid]
#             if currTime != timestamp and currTime < timestamp:
#                 r = mid
#             else:
#                 l = l + 1
#         if bucket[l] is None:
#             return ""
#         else:
#             print(bucket)
#             print(l)
#             return bucket[l][1]
        
        # return self.map[key]
        
        
        