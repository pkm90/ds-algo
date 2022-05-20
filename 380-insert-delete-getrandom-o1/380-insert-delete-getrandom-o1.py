import random

class RandomizedSet:

    def __init__(self):
        self.mem = {}
        self.arr = []
        self.count = 0

    def insert(self, val: int) -> bool:
        if val in self.mem:
            return False
        self.mem[val] = self.count
        self.count += 1
        self.arr.append(val)
        return True
        
    def remove(self, val: int) -> bool:
        if val in self.mem:
            i = self.mem[val]
            end = self.arr[-1]
            self.mem[val], self.mem[end] = self.mem[end], self.mem[val]
            self.arr[i], self.arr[-1] = self.arr[-1], self.arr[i]
            self.arr.pop()
            self.count -= 1
            del self.mem[val]
            return True
        else:
            return False
        
    def getRandom(self) -> int:
        choice = random.randint(0, self.count - 1)
        return self.arr[choice]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()