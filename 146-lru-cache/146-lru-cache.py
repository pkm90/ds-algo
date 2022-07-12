###
# do again...
###
# class LRUCache:

#     def __init__(self, capacity: int):
        

#     def get(self, key: int) -> int:
        

#     def put(self, key: int, value: int) -> None:


# class LRUCache:

#     def __init__(self, capacity: int):
        

#     def get(self, key: int) -> int:
        

#     def put(self, key: int, value: int) -> None:

# class LRUCache:

#     def __init__(self, capacity: int):
        

#     def get(self, key: int) -> int:
        

#     def put(self, key: int, value: int) -> None:





































# class ListNode:
#     def __init__(self, key = None, val = None, prev = None, nxt = None):
#         self.key = key
#         self.val = val
#         self.prev = prev
#         self.next = nxt
        
# class LRUCache:

#     def __init__(self, capacity: int):
#         self.cap = capacity
#         self.cache = {}
#         self.head = ListNode()
#         self.tail = ListNode()
#         self.head.next, self.tail.prev = self.tail, self.head

#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1
#         self.remove(self.cache[key])
#         self.insert(self.cache[key])
#         return self.cache[key].val

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.remove(self.cache[key])
#         newNode = ListNode(key = key, val = value)
#         self.insert(newNode)
#         self.cache[key] = newNode
        
#         if len(self.cache) > self.cap:
#             lru = self.tail.prev
#             self.remove(lru)
#             del self.cache[lru.key]
            
#     def insert(self, n):
#         h = self.head.next
#         n.next, n.prev = h, self.head
#         self.head.next, h.prev = n, n
        
#     def remove(self, n):
#         # prev, nxt = n.prev, n.next
#         # n.prev.next, n.next.prev = n.next, n.prev
#         n.next.prev, n.prev.next = n.prev, n.next


#################################


class Node:
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            self.delete(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
        newNode = Node(key = key, val = value)
        self.cache[key] = newNode
        self.insert(newNode)
        
        if len(self.cache) > self.cap:
            lru = self.tail.prev
            self.delete(lru)
            del self.cache[lru.key]
            
    def insert(self, node):
        node.next, node.prev = self.head.next, self.head
        self.head.next.prev, self.head.next = node, node
        
    def delete(self, node):
        # node.prev.next, node.next.prev = node.next, node.prev
        node.next.prev, node.prev.next = node.prev, node.next



################


# class Node:
#     def __init__(self, key = None, val = None):
#         self.key = key
#         self.val = val
#         self.next = None
#         self.prev = None

# class LRUCache:

#     def __init__(self, capacity: int):
#         self.cap = capacity
#         self.cache = {}
#         self.head = Node()
#         self.tail = Node()
#         self.head.next, self.tail.prev = self.tail, self.head
    
#     def insert(self, node):
#         node.prev, node.next = self.head, self.head.next
#         self.head.next.prev, self.head.next = node, node
        
#     def delete(self, node):
#         prev, nxt = node.prev, node.next
#         prev.next, nxt.prev = nxt, prev
#         # node.prev.next, node.next.prev = node.next, node.prev
        
#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1
#         self.delete(self.cache[key])
#         self.insert(self.cache[key])
#         return self.cache[key].val

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.delete(self.cache[key])
#         newNode = Node(key = key, val = value)
#         self.insert(newNode)
#         self.cache[key] = newNode
        
#         if len(self.cache) > self.cap:
#             lru = self.tail.prev
#             self.delete(lru)
#             del self.cache[lru.key]
    
        
        ###############

# class Node:
#     def __init__(self, val, key):
#         self.val = val
#         self.key = key
#         self.next = None
#         self.prev = None
        
# class LRUCache:

#     def __init__(self, capacity: int):
#         self.cap = capacity
#         self.cache = {}
#         self.head = Node(val = None, key = None)
#         self.tail = Node(val = None, key = None)
#         self.head.next, self.tail.prev = self.tail, self.head

#     def get(self, key: int) -> int:
#         if key in self.cache:
#             self.delete(self.cache[key])
#             self.insert(self.cache[key])
#             return self.cache[key].val
#         return -1

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.delete(self.cache[key])
#         self.cache[key] = Node(val = value, key = key)            
#         self.insert(self.cache[key])
        
#         if len(self.cache) > self.cap:
#             lru = self.tail.prev
#             self.delete(lru)
#             del self.cache[lru.key]
        
#     def insert(self, node):
#         node.prev, node.next = self.head, self.head.next
#         self.head.next.prev, self.head.next = node, node # !!!!if set self.head.next before self.head.next.prev then errors
#         # prev, nxt = self.head, self.head.next
#         # node.prev, node.next = prev, nxt
#         # prev.next, nxt.prev = node, node
        
#     def delete(self, node):
#         prev, nxt = node.prev, node.next
#         prev.next, nxt.prev = nxt, prev

     
        ###################

# class Node:
#     def __init__(self, key = None, val = None):
#         self.key = key
#         self.val = val
#         self.prev = None
#         self.next = None
    
# class LRUCache:

#     def __init__(self, capacity: int):
#         self.cap = capacity
#         self.cache = {}
#         self.head = Node()
#         self.tail = Node()
#         self.head.next, self.tail.prev = self.tail, self.head

#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1
#         self.remove(self.cache[key])
#         self.insert(self.cache[key])
#         return self.cache[key].val

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.remove(self.cache[key])
#         self.cache[key] = Node(key = key, val = value)
#         self.insert(self.cache[key])
        
#         if len(self.cache) > self.cap:
#             lru = self.tail.prev
#             self.remove(lru)
#             del self.cache[lru.key]
        
#     def insert(self, node):
#         prev, nxt = self.head, self.head.next
#         prev.next, nxt.prev = node, node
#         node.next, node.prev = nxt, prev
        
#     def remove(self, node):
#         prev, nxt = node.prev, node.next
#         prev.next, nxt.prev = nxt, prev 
    
    
    ###############################
    

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

