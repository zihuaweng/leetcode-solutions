# https://leetcode.com/problems/binary-tree-level-order-traversal/
# 使用queue将一层的结果推入，然后打印这一层的每一个结果时把左分支和右分支都推入。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = collections.deque([root])
        
        while queue:
            res_val = []
            for _ in range(len(queue)):
                node = queue.popleft()
                res_val.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(res_val)
            
        return res
                