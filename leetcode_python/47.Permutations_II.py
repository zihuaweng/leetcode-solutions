#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/permutations-ii/
# https://leetcode.com/problems/subsets/discuss/27281/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
# 和46的区别是有重复的数字
# 第一步：排序
# 第二步：dfs
# dfs里面需要判断重复的数字跳过，模板和90一样
# 如果前面的数字是一样的，而且已经被使用了，那就跳过

# 需要注意的是，这里的判断是：if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
# 这里使用not used[i-1] 和 used[i-1] 会得到一样的结果，但是not used[i-1]会更高效
# 因为not used[i-1]意思是，如果前面和当前值一样，那我就选前面的，所以每遇到相同的值，代码只会选择第一个，无论后面有多少个重复的值他都不会跑，节省时间。
# 但是used[i-1]意思是，如果前面的使用了，我就不跑当前，所以所有重复的数字都会跑，需要跑的迭代越多，浪费时间。
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [0] * len(nums)
        nums.sort()
        self.helper(nums, used, [], res)
        return res

    def helper(self, nums, used, temp, res):

        if len(temp) == len(nums):
            res.append(temp[:])
            return
        for i in range(len(used)):
            if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]): # 在这里判断重复的数字
                continue
            used[i] = 1
            self.helper(nums, used, temp + [nums[i]], res)
            used[i] = 0