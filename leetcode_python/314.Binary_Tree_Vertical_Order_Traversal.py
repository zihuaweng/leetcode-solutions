#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/binary-tree-vertical-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        """
        
           3
          /\
         /  \
         9  20
            /\
           /  \
          15   7 
        -1 
          0. 1. 2
          
        1. keep track of the vertical order of the tree, the root is 0, left -= 1 right += 1
        2. treverse the tree by horizontal levels, bfs, deque
        3. add the val to the res, return by vertical order.
        """
        if not root:
            return []
        
        graph = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])
        
        while queue:
            node, order = queue.popleft()
            graph[order].append(node.val)
            if node.left:
                queue.append((node.left, order-1))
            if node.right:
                queue.append((node.right, order+1))
                
        res = []
        for key in sorted(graph):
            res.append(graph[key])
            
        return res