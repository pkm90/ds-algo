class Solution:
    def minDeletions(self, s: str) -> int:
        
        
        # grab freqs
        chars = Counter(s)
        visit = set()
        res = 0
        
        print(chars)
        
        # continue iterating until freqs are all unique
        while True:
            visit.clear()
            numUnique = len(chars)
            for char, count in chars.items():
                if count == 0:
                    numUnique -= 1
                    continue
                if count in visit:
                    chars[char] -= 1
                    res += 1
                    break
                visit.add(count)
            if len(visit) == numUnique:
                print(chars)
                return res
        # return number of iterations
        
        