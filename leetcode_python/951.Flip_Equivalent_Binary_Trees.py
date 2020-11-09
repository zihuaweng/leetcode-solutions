# https://leetcode.com/problems/flip-equivalent-binary-trees/
# Time complexity: O(n)
# Space complexity: O(h)

# self.flipEquiv(root1.left,root2.left) and self.flipEquiv(root1.right,root2.right)
# 这里也是需要的因为输入如果是[1,2,3], [1,2,3],其实是没有反转的

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None or root1.val != root2.val:
            return False
        else:
            return self.flipEquiv(root1.left,
                                  root2.right) and self.flipEquiv(root1.right,
                                                                  root2.left) \
                   or \
                   self.flipEquiv(root1.left,
                                  root2.left) and self.flipEquiv(root1.right,
                                                                 root2.right)
