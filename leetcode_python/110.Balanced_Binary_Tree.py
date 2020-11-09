# https://leetcode.com/problems/balanced-binary-tree/
# Time complexity: O(n)
# Space complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    def __init__(self):
        self.res = True

    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        self.helper(root)
        return self.res

    def helper(self, root):
        if root is None:
            return 0
        l = self.helper(root.left)
        r = self.helper(root.right)
        if abs(l - r) > 1:
            self.res = False
        return max(l, r) + 1


class Solution2:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.helper(root) != -1

    def helper(self, root):
        if root is None:
            return 0
        l = self.helper(root.left)
        r = self.helper(root.right)
        if l == -1 or r == -1 or abs(l - r) > 1:
            return -1
        return max(l, r) + 1
