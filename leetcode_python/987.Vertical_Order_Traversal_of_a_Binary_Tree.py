#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# 使用recursion也可以，排序的时候可以使用
# array.sort(key = lambda el: [el[0], el[1], el[2]])


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res

        loc = collections.defaultdict(list)
        queue = [(0, root)]
        while queue:
            temp = []
            new = collections.defaultdict(list)
            for s, node in queue:
                if node.left:
                    temp.append((s - 1, node.left))
                if node.right:
                    temp.append((s + 1, node.right))
                new[s].append(node.val)
            for key, val in new.items():
                loc[key].extend(sorted(val))
            queue = temp

        return [loc[i] for i in sorted(loc)]

