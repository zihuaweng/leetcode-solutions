# https://leetcode.com/problems/maximum-product-subarray/
# 因为有正负数，所以每遇到一个新的数字要记录最大值和最小值，根据新数字的正负得到新的最大值和最小值
# 注意更新最大值和最小值的时候值被改变的影响更新结果，所以要有max_temp ／ min_temp这两个变量

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_to_cur = nums[0]
        min_to_cur = nums[0]
        max_product = nums[0]

        for i in nums[1:]:
            if i > 0:
                max_temp = max(max_to_cur * i, i)
                min_temp = min(min_to_cur * i, i)
            else:
                max_temp = max(min_to_cur * i, i)
                min_temp = min(max_to_cur * i, i)
            max_product = max(max_temp, max_product)
            max_to_cur, min_to_cur = max_temp, min_temp

        return max_product


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_p = nums[0]
        min_p = nums[0]
        total = nums[0]
        for num in nums[1:]:
            if num < 0:
                max_p, min_p = min_p, max_p

            min_p = min(min_p * num, num)
            max_p = max(max_p * num, num)
            total = max(total, max_p)

        return total
