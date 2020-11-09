#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(n)
# Space complexity: O()

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        pre_order = []
        
        def dfs(root):
            if not root:
                pre_order.append('#')
            else:
                pre_order.append(str(root.val))
                dfs(root.left)
                dfs(root.right)
                
        dfs(root)
                
        return ','.join(pre_order)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        queue = collections.deque(data.split(','))
        
        def dfs():
            val = queue.popleft()
            if val == '#':
                return None
            else:
                val = int(val)
                node = TreeNode(val)
                node.left = dfs()
                node.right = dfs()
                
            return node
        
        return dfs()
                

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))