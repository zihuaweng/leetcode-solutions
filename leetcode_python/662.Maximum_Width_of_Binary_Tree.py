# https://leetcode.com/problems/maximum-width-of-binary-tree/

# if count root as No.1 then for each node (n), it have left child node (2n)
# and right node (2n+1)
# For each level, the longest path will be the last node in queue - first node in queue + 1


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        queue = collections.deque([(root, 0)])
        while queue:
            res = max(res, queue[-1][1] - queue[0][1] + 1)
            n = len(queue)
            for _ in range(n):
                node, val = queue.popleft()
                if node.left:
                    queue.append((node.left, val * 2))
                if node.right:
                    queue.append((node.right, val * 2 + 1))
        return res
