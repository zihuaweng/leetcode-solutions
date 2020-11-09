# https://leetcode.com/problems/binary-tree-inorder-traversal/
# 二叉树的中序遍历
# 遍历到最左边然后打印，再遍历右边
# Time complexity: O(n)
# Space complexity: O(h) # 感觉这里存了res，所以应该是O(n)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root is None:
            return

        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right

        return res