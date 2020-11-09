# https://leetcode.com/problems/sort-transformed-array/

class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int,
                             c: int) -> List[int]:
        nums = [a * x * x + b * x + c for x in nums]
        p1 = 0
        p2 = len(nums) - 1
        # decide which side to start filling res.
        # if a < 0, value in two sides will be smaller, so we fill res from beginning
        # if a > 0, value in two sides will be larger, so we fill res from the end
        i, d = (p1, 1) if a < 0 else(p2, -1)

        res = [0] * len(nums)
        while p1 <= p2:
            if nums[p1] * -d > nums[p2] * -d:
                res[i] = nums[p1]
                p1 += 1
            else:
                res[i] = nums[p2]
                p2 -= 1
            i += d

        return res