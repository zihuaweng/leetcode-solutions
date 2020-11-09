#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        self.pre_sum = [0]
        pre = 0
        for n in nums:
            pre += n
            self.pre_sum.append(pre)

    def sumRange(self, i: int, j: int) -> int:
        # print(self.pre_sum)
        return self.pre_sum[j+1] - self.pre_sum[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)