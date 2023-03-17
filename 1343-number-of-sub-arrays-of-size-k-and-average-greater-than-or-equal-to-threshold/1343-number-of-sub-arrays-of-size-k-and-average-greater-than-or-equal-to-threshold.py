class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        
        # subarray uses adjacent elements
        # avg >= threshold
        
        res = 0
        l = 0
        total = sum(arr[0:k])
        # print(arr[0:k])
        # print(len(arr))
        for r in range(k, len(arr)):
            # 0 : 3 + 1
            # 0 : 4
            # 0,1,2,3
            # print(len(arr[l:r + 1]))
            # print(arr[l:r])
            # print(r)
            if (total / k) >= threshold:
                res += 1
            
            # print(r)
            total = total - arr[l] + arr[r]
            l += 1
            
        if (total / k) >= threshold:
                res += 1
                
        return res
        

        # k * n
            