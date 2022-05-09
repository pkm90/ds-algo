###
# do again...
###
# class LRUCache:

#     def __init__(self, capacity: int):
        

#     def get(self, key: int) -> int:
        

#     def put(self, key: int, value: int) -> None:
        

class Node:
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        curr = self.cache[key]
        currVal = self.cache[key].val
        self.remove(curr)
        self.insert(Node(key = key, val = currVal))
        return currVal

    def put(self, key: int, value: int) -> None:
        # newNode = Node(key = key, val = value)
        if key in self.cache:
            self.remove(self.cache[key])
        self.insert(Node(key = key, val = value))
        if len(self.cache) > self.cap:
            self.remove(self.tail.prev)
        
    def insert(self, node):
        oldHead = self.head.next
        oldHead.prev, self.head.next = node, node
        node.prev, node.next = self.head, oldHead
        self.cache[node.key] = node
        # print('added', node.key)
        
    def remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        del self.cache[node.key]
        # print('removed', node.key)
        
        # print(key)
        # oldNode = self.cache.get(key, None)
        # if oldNode:
        #     # oldNode = self.cache[key]
        #     oldNode.prev.next, oldNode.next.prev = oldNode.next, oldNode.prev
        # else:
        #     oldNode = self.tail.prev
        #     print(oldNode.val)
        #     oldNode.prev.next, oldNode.next.prev = oldNode.next, oldNode.prev

        

    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

# class Node:
#     def __init__(self, key = None, value = None, prev = None, nxt = None):
#         self.key = key
#         self.val = value
#         self.prev = prev
#         self.nxt = nxt
        
# class LRUCache:

#     def __init__(self, capacity: int):
#         self.cap = capacity
#         self.head = Node()
#         self.tail = Node()
#         self.cache = {}
#         self.head.nxt, self.tail.prev = self.tail, self.head
        
#     def get(self, key: int) -> int:
#         # print('getting', key, self.cache)
#         if key in self.cache:
#             temp = self.cache[key]
#             self.remove(key)
#             self.insert(key = key, value = temp.val)
#             return self.cache[key].val
#         else:
#             return -1
        
#     def put(self, key: int, value: int) -> None:
#         # curr = Node(key = key, value = value)
#         self.remove(key)
#         self.insert(key, value)
#         if len(self.cache) > self.cap:
#             # temp = self.head.nxt.key
#             self.remove(self.tail.prev.key)
#         # print(self.cache)
    
#     def insert(self, key, value):
#         recent = self.head.nxt
#         curr = Node(key = key, value = value, prev = self.head, nxt = recent)
#         # print(self.right, self.right.nxt)
#         self.head.nxt, recent.prev = curr, curr
#         self.cache[key] = curr
#         # print(self.cache)
        
#     def remove(self, key):
#         if key in self.cache:
#             curr = self.cache[key]
#             nxt, prev = curr.nxt, curr.prev
#             nxt.prev, prev.nxt = prev, nxt        
#             del self.cache[key]
    
######################################
    
# class Node:
#     def __init__(self, val = None, key = None):
#         self.val = val
#         self.key = key
#         self.next = None
#         self.prev = None
    
# class LRUCache:

#     def __init__(self, capacity: int):
#         self.cap = capacity
#         self.data = {}
#         self.least = Node()
#         self.most = Node()
#         self.least.prev, self.most.next = self.most, self.least

#     def get(self, key: int) -> int:
#         print('getting', key)
#         if key in self.data:
#             node = self.data[key]
#             self.refresh(node)
#             return self.data[key].val
#         return -1

#     def put(self, key: int, value: int) -> None:
#         print('putting', key, value)
#         if key in self.data:
#             self.remove(self.data[key])
#         node = Node(val = value, key = key)
#         self.data[key] = node
#         self.refresh(node)
        
#         if len(self.data) > self.cap:
#             print('removing cause capacity', key)
#             self.remove(self.least.prev)
                
#     def refresh(self, node):
#         curr = node
#         if curr.prev or curr.next:
#             prev, nxt = curr.prev, curr.next
#             prev.next, nxt.prev = nxt, prev

#         head = self.most.next
#         self.most.next, head.prev = curr, curr
#         curr.prev, curr.next = self.most, head
        
#     def remove(self, node):
#         curr = node
#         prev, nxt = curr.prev, curr.next
#         prev.next, nxt.prev = nxt, prev
#         del self.data[curr.key]
        


# # Your LRUCache object will be instantiated and called as such:
# # obj = LRUCache(capacity)
# # param_1 = obj.get(key)
# # obj.put(key,value)

