# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# 前序遍历第一个就是root，只要找到root在中序遍历的位置，左边就是root的左分支，右边是root的右分支
# 然后递归去实现

# Time complexity: O(n^2)
# Space complexity: O(n^2)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        i = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:1 + i], inorder[:i])
        root.right = self.buildTree(preorder[1 + i:], inorder[i + 1:])
        return root
