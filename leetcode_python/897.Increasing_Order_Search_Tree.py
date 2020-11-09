# https://leetcode.com/problems/increasing-order-search-tree/
# Time complexity: O(n)
# Space complexity: O(1)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:

    def __init__(self):
        self.head = None
        self.pre = None

    def increasingBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        self.increasingBST(root.left)
        if self.pre is not None:
            root.left = None
            self.pre.right = root
        if self.head is None:
            self.head = root
        self.pre = root
        self.increasingBST(root.right)
        return self.head


class Solution2:

    def increasingBST(self, root: TreeNode) -> TreeNode:
        res = self.helper(root, None)
        return res

    def helper(self, root, tail):
        if root is None:
            return tail
        res = self.helper(root.left, root)
        root.left = None
        root.right = self.helper(root.right, tail)
        return res
