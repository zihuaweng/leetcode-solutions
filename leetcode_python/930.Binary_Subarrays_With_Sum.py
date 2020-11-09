# https://leetcode.com/problems/binary-subarrays-with-sum/
# subarry, sliding window


# 第一种方法，dictionary，参考 3.Longest_Substring_Without_Repeating_Characters.py
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        res = 0
        pre_sum = 0
        d = collections.defaultdict(int)
        d[0] = 1
        for val in A:
            pre_sum += val
            res += d[pre_sum-S]
            d[pre_sum] += 1
        return res


# 第二种方法， sliding window，subarray, 如果是at most k distinct的话，可以使用sliding window，但是是extract k distinct的话，就需要用atMost(k)-atMost(k-1)
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        return self.atMost(A, S) - self.atMost(A, S-1)
        
    def atMost(self, A, S):
        res = 0
        i = 0
        pre_sum = 0
        for j, val in enumerate(A):
            pre_sum += val
            while pre_sum > S and i <= j:
                pre_sum -= A[i]
                i += 1
            res += j-i+1
        return res