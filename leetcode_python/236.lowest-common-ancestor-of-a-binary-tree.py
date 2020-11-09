# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# 最近公共祖先


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        # 如果找到了目标就返回这个root
        if root is p or root is q:
            return root

        # 遍历左右子节点，如果没有目标，返回None，有结果返回当前root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 如果两边都有结果，返回着root （这个就是最近祖先）
        if left and right:
            return root
        # 如果只有左边有结果，返回左边 （最近祖先往上走就是只有一边的结果）
        if left:
            return left
        # 如果只有右边有结果，返回右边（最近祖先往上走就是只有一边的结果）
        if right:
            return right
