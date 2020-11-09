#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
# refer to java!

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#  O(nlogn)
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        head = TreeNode(preorder[0])
        index = self.bs(preorder[1:], preorder[0])
        head.left = self.bstFromPreorder(preorder[1:index + 1])
        head.right = self.bstFromPreorder(preorder[index + 1:])
        return head

    def bs(self, arr, value):
        i = 0
        j = len(arr)
        while i < j:
            mid = (i + j) // 2
            if arr[mid] <= value:
                i = mid + 1
            else:
                j = mid
        return i


#  O(n)
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        head = TreeNode(preorder[0])
        stack = [head]
        for i in range(1, len(preorder)):
            node = TreeNode(preorder[i])
            if (stack and stack[-1].val > preorder[i]):
                stack[-1].left = node
            else:
                parent = stack.pop()
                while stack and stack[-1].val < preorder[i]:
                    parent = stack.pop()
                parent.right = node
            stack.append(node)
        return head
