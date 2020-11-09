# https://leetcode.com/problems/subarrays-with-k-different-integers/
# 


class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        """
        if we need to get extactlly k distinct char, we can use
        atMost(k) - atMost(k-1)
        so when we calculate atMost(k), we can use sliding window
        """
        return self.subarraysWithAtMostKDistinct(A, K) - self.subarraysWithAtMostKDistinct(A, K-1)
        
    def subarraysWithAtMostKDistinct(self, A, K):
        d = {}
        res = 0
        i = 0
        for j, val in enumerate(A):
            d[val] = d.get(val, 0) + 1
            
            while len(d) > K:
                d[A[i]] -= 1
                if d[A[i]] == 0:
                    del d[A[i]]
                i += 1
            
            # 这里我们需要计算个数, 以j为右指针，从i-j一共有j-i+1个组合，刚好是这个subarray的长度
            res += j-i+1
        return res