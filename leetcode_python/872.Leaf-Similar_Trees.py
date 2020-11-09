# https://leetcode.com/problems/leaf-similar-trees/
# Time complexity: O(n)
# Space complexity: O(h1+h2)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        # return list(self.dfs(root1)) == list(self.dfs(root2))
        return all(a == b for a, b in itertools.zip_longest(self.dfs(root1), self.dfs(root2)))

    def dfs(self, root):
        if root is None:
            return
        if root.right is None and root.left is None:
            yield root.val
        yield from self.dfs(root.left)
        yield from self.dfs(root.right)


