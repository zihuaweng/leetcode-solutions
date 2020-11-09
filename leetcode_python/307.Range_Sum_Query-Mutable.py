#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(logn)
# Space complexity: O()

# https://leetcode.com/problems/range-sum-query-mutable/

# 需要使用SegmentTree数据结构
# SegmentTree主要用在需要求前几个数的的sum
# 一般使用需要O(n)
# SegmentTree O(logn)

class SegmentTreeNode:
    def __init__(self, start, end, val):
        self.start = start
        self.end = end
        self.val = val
        self.left = None
        self.right = None


class NumArray:

    def __init__(self, nums: List[int]):
        if nums:
            self.root = self._build_tree(0, len(nums) - 1, nums)

    def _build_tree(self, start, end, nums):
        if start == end:
            return SegmentTreeNode(start, end, nums[start])
        mid = (start + end) >> 1
        left = self._build_tree(start, mid, nums)
        right = self._build_tree(mid + 1, end, nums)
        root = SegmentTreeNode(start, end, left.val + right.val)
        root.left = left
        root.right = right
        return root

    def update(self, i: int, val: int) -> None:
        self._update(self.root, i, val)

    def _update(self, root, index, val):
        if root.start == index and root.end == index:
            root.val = val
            return
        mid = (root.start + root.end) >> 1
        if index <= mid:
            self._update(root.left, index, val)
        else:
            self._update(root.right, index, val)
        root.val = root.left.val + root.right.val

    def sumRange(self, i: int, j: int) -> int:
        return self._sum(self.root, i, j)

    def _sum(self, root, i, j):
        if i == root.start and j == root.end:
            return root.val
        mid = (root.start + root.end) >> 1
        if mid >= j:
            return self._sum(root.left, i, j)
        elif mid < i:
            return self._sum(root.right, i, j)
        else:
            return self._sum(root.left, i, mid) + self._sum(root.right, mid + 1, j)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

# BIT
class NumArray:

    def __init__(self, nums: List[int]):
        self.tree = [0] * (len(nums) + 1)
        self.nums = [0] * len(nums)

        for i, num in enumerate(nums):
            self.update(i, num)

    def update(self, i: int, val: int) -> None:
        diff = val - self.nums[i]
        self.nums[i] = val
        i += 1
        while i < len(self.tree):
            self.tree[i] += diff
            i += i & -i

    def getsum(self, i):
        s = 0
        i += 1
        while i > 0:
            s += self.tree[i]
            i -= i & -i

        return s

    def sumRange(self, i: int, j: int) -> int:
        return self.getsum(j) - self.getsum(i - 1)
