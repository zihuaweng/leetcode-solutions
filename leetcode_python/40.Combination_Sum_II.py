#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/combination-sum-ii/

# 这里需要注意的是有重复，每个数只能用一次，所以从index开始，如果有相同的就要跳过，不然会有重复使用
# 因为要判断是否一致，最简单就是闲sort一下

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.helper(target, candidates, 0, [], res)
        return res

    def helper(self, target, candidates, idx, tmp, res):
        if target == 0:
            res.append(tmp)
            return

        if target < 0:
            return

        for i in range(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i - 1]: # 这里需要判断重复，和90题一样
                continue
            c = candidates[i]
            self.helper(target - c, candidates, i + 1, tmp + [c], res)


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        n = len(candidates)
        for i in range(1<<n):
            cur_sum = 0
            temp = []
            for j in range(n-1, -1, -1):
                if i & (1<<j):
                    if j > 0 and candidates[j] == candidates[j-1]:
                        continue
                    cur_sum += candidates[j]
                    temp.append(candidates[j])
            if cur_sum == target:
                res.append(temp)