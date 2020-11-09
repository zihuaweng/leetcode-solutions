# https://leetcode.com/problems/valid-triangle-number/

# O(n^2)
# This is the same as 3 sum


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        for i in range(2, n):
            p1 = 0
            p2 = i - 1
            while p1 < p2:
                if nums[p1] + nums[p2] > nums[i]:
                    # if p1 and p2 could be valid triangle, then all numbers
                    # from p1 to p2-1 could form valid triangle with p2, so
                    # count add p2 - p1 and p2 need to move to left.
                    count += p2 - p1
                    p2 -= 1
                else:
                    p1 += 1
        return count
