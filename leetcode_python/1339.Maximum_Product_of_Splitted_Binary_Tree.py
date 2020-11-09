# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxProduct(self, root: TreeNode) -> int:
        
        self.res = 0
        total = 0
        
        def get_sum(root):
            if not root:
                return 0
            
            left = get_sum(root.left)
            right = get_sum(root.right)
            self.res = max([self.res, left*(total-left), right*(total-right)])
            
            return root.val + left + right
        
        total = get_sum(root)
        get_sum(root)
        
        return self.res % (10**9 + 7)