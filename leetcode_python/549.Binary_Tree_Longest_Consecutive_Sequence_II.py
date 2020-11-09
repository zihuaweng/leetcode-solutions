#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii

def longestConsecutive(self, root: TreeNode) -> int:
    def longest_path(root):
        if not root:
            return 0, 0
        inc, dec = 1, 1
        l_inc, l_dec = longest_path(root.left)
        r_inc, r_dec = longest_path(root.right)
        if root.left:
            if root.left.val == root.val + 1:
                inc = max(inc, 1 + l_inc)
            if root.left.val == root.val - 1:
                dec = max(dec, 1 + l_dec)
        if root.right:
            if root.right.val == root.val + 1:
                inc = max(inc, 1 + r_inc)
            if root.right.val == root.val - 1:
                dec = max(dec, 1 + r_dec)
        res[0] = max(res[0], inc + dec - 1)
        return (inc, dec)

    res = [0]
    longest_path(root)
    return res[0]