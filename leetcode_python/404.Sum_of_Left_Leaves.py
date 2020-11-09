#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class Solution:

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right) # 重复计算
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)


# 更快
class Solution2:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.res = 0
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return
        if root.left and not root.left.left and not root.left.right:
            self.res += root.left.val
        self.helper(root.left)
        self.helper(root.right)

