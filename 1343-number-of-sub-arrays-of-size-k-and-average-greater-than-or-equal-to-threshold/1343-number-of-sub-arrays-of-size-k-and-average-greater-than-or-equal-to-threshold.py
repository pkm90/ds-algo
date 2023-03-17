class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        
        # subarray uses adjacent elements
        # avg >= threshold
        
        res = 0
        l = 0
        total = sum(arr[0:k])
        for r in range(k, len(arr)):

            if (total / k) >= threshold:
                res += 1
            
            total = total - arr[l] + arr[r]
            l += 1
            
        if (total / k) >= threshold:
                res += 1
                
        return res

    