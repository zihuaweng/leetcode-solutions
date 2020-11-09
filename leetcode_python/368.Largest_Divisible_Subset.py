#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/largest-divisible-subset/

# 思路：
# 因为需要任意两个值都能整除，所以我们只要知道新的数字，和现有的数组里最大的值能不能整除就可以了。
# 所以数组一定是要排序的才能做到上一点

# 第一个方法是每经过一个数字，就加入当前的最长的列表，所以里面其实是有冗余的
# 首先排序
# 然后遍历，每个数字都需要查看现有的列表中最后一个数字是不是整除。
# 最后选择最长的一个列表

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        dp = [[]]
        for n in sorted(nums):
            dp.append(max((s for s in dp if not s or n % s[-1] == 0), key=len) + [n])
        return max(dp, key=len)


# 第二个方法
# dp
# 保存一个count列表，记录当前数字最长的set
# 一个pre，记录前面一个index是什么，用于返回最后的结果。
# 所以，每经过一个数字，我们就看之前的每个数字，有没有可以和当前数字凑一个更长的列表

# 例如：
# 1 2 4 8
# index用来记录所有最长的那个数字的index
# max_val表示的是最长的长度，用来更新index
# count = [1, 1, 1, 1]
# pre = [-1, -1, -1, -1] (因为需要用-1来判断终止)
# 最后结果是
# max_val = 4
# index = 3
# count = [1, 2, 3, 4]
# pre = [-1, 0, 1, 2]

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        l = len(nums)
        count = [1] * l
        pre = [-1] * l
        max_val = 0
        index = -1
        nums.sort()
        for i in range(l):
            for j in range(i - 1, -1, -1):
                if nums[i] % nums[j] == 0:
                    if count[j] + 1 > count[i]:
                        count[i] = count[j] + 1
                        pre[i] = j
            if max_val < count[i]:
                max_val = count[i]
                index = i

        res = []
        while index != -1:
            res.append(nums[index])
            index = pre[index]

        return res