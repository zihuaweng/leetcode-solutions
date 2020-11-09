# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Time complexity: O(n)
# Space complexity: O(n)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        depth = self.helper(root, 0)
        return depth

    def helper(self, root, depth):
        if root is None:
            return depth
        depth += 1
        l_depth = self.helper(root.left, depth)
        r_depth = self.helper(root.right, depth)
        return max(l_depth, r_depth)


class Solution2:
    def maxDepth(self, root):
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
