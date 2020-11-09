# https://leetcode.com/problems/delete-node-in-a-bst/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            min_node = root.right
            while min_node.left:
                min_node = min_node.left
            
            # 唯一的区别：
            min_node.left = root.left
            return root.right
        
        return root


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            min_node = root.right
            while min_node.left:
                min_node = min_node.left
            
            # 唯一的区别：
            root.val = min_node.val
            root.right = self.deleteNode(root.right, min_node.val)
        
        return root