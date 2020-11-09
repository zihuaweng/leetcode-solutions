# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

# Time complexity: O(n^2)
# Space complexity: O(n^2)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre:
            return
        root = TreeNode(pre.pop(0))
        if not pre:
            return root
        L = post.index(pre[0])
        root.left = self.constructFromPrePost(pre[:L+1], post[:L+1])
        root.right = self.constructFromPrePost(pre[L+1:], post[L+1:-1])
        return root