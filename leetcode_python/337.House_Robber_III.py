# coding: utf-8

# https://leetcode.com/problems/house-robber-iii/

# https://www.youtube.com/watch?v=-i2BFAU25Zk

# Time complexity: O()
# Space complexity: O()

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        """
        1. each node could be robbed or not robbed, [r, n_r]
        2. if the node is robbed: total = curr + not rob left child + not rob right child
        3. if the node is not robbed:   children could be rob or not rob,  total = max(left child) + max(right child)
        4. result = max(r_root, n_r_root)

             3      [r, n_r]   r: current + n_r_left + n_r_right       n_r = max(r_left, n_r_left) + max(r_right, n_r_right) 
            / \
           2   3     
            \   \ 
             3   1
        """       
        return max(self.helper(root))

    def helper(self, root):
        if not root:
            return [0, 0]
        left = self.helper(root.left)
        right = self.helper(root.right)
        res = [0, 0]
        res[0] = max(left) + max(right)
        res[1] = root.val + left[0] + right[0]
        return res


class Solution:
    def rob(self, root: TreeNode) -> int:
        r, nr = self.helper(root)
        return max(r, nr)

    def helper(self, root):
        if not root:
            return 0, 0
        l_r, l_nr = self.helper(root.left)
        r_r, r_nr = self.helper(root.right)
        r = l_nr + r_nr + root.val
        nr = max(l_r, l_nr) + max(r_r, r_nr)
        return r, nr


