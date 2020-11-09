#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(2^N) where N = 4.
# Space complexity: O()


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        return self.dfs(nums)

    def dfs(self, nums):
        # 只剩一个返回
        if len(nums) == 1:
            # if 23 < nums[0] < 25:
            #     print(nums)
            if abs(nums[0] - 24) < 0.00001:
                return True
            else:
                return False

        # 每次抽取两个
        length = len(nums)
        for i in range(length - 1):
            for j in range(i + 1, length):
                next_nums = []
                for k in range(length):
                    if k != i and k != j:
                        next_nums.append(nums[k])
                for n in self.compute(nums[i], nums[j]):
                    if self.dfs(next_nums + [n]):
                        return True
        return False

    def compute(self, a, b):
        res = [a + b, a - b, b - a, a * b]
        if a != 0:
            res.append(b / a)
        if b != 0:
            res.append(a / b)
        return res