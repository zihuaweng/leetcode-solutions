#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


# <0,-1> can allow it to return true when the runningSum%k=0,
# In addition, it also avoids the first element of the array is the multiple of k, since 0-(-1)=1 is not greater than 1.
# I think it's really beautiful and elegant here!

# (a+(n*x))%x is same as (a%x)

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remain_map = {}
        remain_map[0] = -1
        pre_sum = 0
        for i in range(len(nums)):
            pre_sum += nums[i]
            if k != 0:
                r = pre_sum % k
            else:
                r = pre_sum

            if r in remain_map:
                if i - remain_map[r] > 1:
                    return True
            else:
                remain_map[r] = i

        return False


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remain_map = {}
        remain_map[0] = -1
        pre_sum = 0
        for i in range(len(nums)):
            pre_sum += nums[i]
            if k != 0:
                pre_sum %= k

            if pre_sum in remain_map:
                if i - remain_map[pre_sum] > 1:
                    return True
            else:
                remain_map[pre_sum] = i

        return False

# 另一种方法
# https://leetcode.com/problems/continuous-subarray-sum/discuss/99503/Need-to-pay-attention-to-a-lot-of-corner-cases...