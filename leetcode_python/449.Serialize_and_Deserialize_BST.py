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

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        pre_order = []
        
        def dfs(root):
            if not root:
                return None
            pre_order.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
            
        dfs(root)
        return ','.join(pre_order)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        
        queue = collections.deque(data.split(','))
        
        def dfs(min_val, max_val):
            if not queue:
                return None
            val = int(queue[0])
            if val < min_val or val > max_val:
                return None
            val = int(queue.popleft())
            node = TreeNode(val)
            node.left = dfs(min_val, val)
            node.right = dfs(val, max_val)
            return node
        
        return dfs(float('-inf'), float('inf'))

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans