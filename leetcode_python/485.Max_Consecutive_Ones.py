# https://leetcode.com/problems/max-consecutive-ones/


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        pre_max = 0
        res = 0
        for n in nums:
            if n == 0:
                pre_max = 0
            else:
                pre_max += 1
                res = max(res, pre_max)
        return res



# two pointer
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = -1
        res = 0
        for j, val in enumerate(nums):
            if val == 0:
                i = j
            else:
                res = max(res, j - i)
        return res