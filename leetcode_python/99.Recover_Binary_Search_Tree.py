#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr = []
        self.in_order(root, arr)
        x, y = self.get_nodes(arr)
        x.val, y.val = y.val, x.val
        return root

    def in_order(self, root, arr):
        if not root:
            return
        self.in_order(root.left, arr)
        arr.append(root)
        self.in_order(root.right, arr)

    def get_nodes(self, arr):
        x = None
        y = None
        for i in range(len(arr) - 1):
            if arr[i].val > arr[i + 1].val:
                y = arr[i + 1]
                if not x:
                    x = arr[i]
                else:
                    break
        return x, y



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
                 x
              y1 
            x1
          y2
        x
                 x
         y1      
            x1
                y2
        x        
        
        the inorder treversal
        y2 < x1 < y2
        
        the swap order:
        y1 > x1
        x1 > y2
        """
        self.first = None
        self.second = None
        self.prev = TreeNode(float('-inf'))
        self.dfs(root)
        # print(self.first.val, self.second.val)
        self.first.val, self.second.val = self.second.val, self.first.val
        
        
    def dfs(self, root):
        if not root:
            return
        
        
        
        self.dfs(root.left)
        if root.val < self.prev.val:
            if not self.first:
                self.first = self.prev
                self.second = root
                self.prev = root
            else:
                self.second = root
                return
        else:
            self.prev = root
        self.dfs(root.right)
        
        