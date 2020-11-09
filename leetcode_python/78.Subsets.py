# https://leetcode.com/problems/subsets/
# 典型递归实现题目，每个位置加入有两种选择，加入或者不加入，通过两个递归就能得到结果。


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums:
            return res
        self.helper(nums, res, 0, [])
        return res

    def helper(self, nums, res, i, temp):
        if i == len(nums):
            res.append(temp[:])
            return
        # for i in range(index, len(nums)-1):
        self.helper(nums, res, i + 1, temp)
        self.helper(nums, res, i + 1, temp + [nums[i]])



class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(res, [], 0, nums)
        return res

    def dfs(self, res, temp, start, nums):
        res.append(temp[:])
        for i in range(start, len(nums)):
            self.dfs(res, temp + [nums[i]], i + 1, nums)