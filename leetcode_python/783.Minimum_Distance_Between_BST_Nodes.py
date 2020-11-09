#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


# https://leetcode.com/problems/minimum-distance-between-bst-nodes/

class Solution:
    pre = float('-inf')
    res = float('inf')

    def minDiffInBST(self, root: TreeNode) -> int:
        if not root:
            return
        self.minDiffInBST(root.left)
        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val
        self.minDiffInBST(root.right)
        return self.res