# https://leetcode.com/problems/validate-binary-search-tree/
# 判断是否正常就得到中序遍历的结果，看是不是递增的，如果不是False

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        res = []
        self.helper(root, res)
        for i in range(1, len(res)):
            if res[i] <= res[i - 1]:
                return False
        return True

    def helper(self, root, res):
        if root is None:
            return
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)

    # intacive
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = []
        pre = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre and root.val <= pre.val:
                return False
            pre = root
            root = root.right

        return True


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        #         10
        #         /\
        #        5  15
        #       /\  /\
        #          6  20

        if root is None:
            return True

        return self.dfs(root, float('-inf'), float('inf'))

    def dfs(self, node, min_val, max_val):
        if node is None:
            return True
        if node.val <= min_val or node.val >= max_val:
            return False
        return self.dfs(node.left, min_val, node.val) and self.dfs(node.right, node.val, max_val)
