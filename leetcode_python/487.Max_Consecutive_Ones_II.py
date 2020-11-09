# https://leetcode.com/problems/max-consecutive-ones-ii/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 1
        j = 0
        res = 0
        for i, val in enumerate(nums):
            if val == 0:
                c -= 1
                
            while c < 0:
                if nums[j] == 0:
                    c += 1
                j += 1
            res = max(res, i-j+1)
        return res