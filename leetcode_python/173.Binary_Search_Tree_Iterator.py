# https://leetcode.com/problems/binary-search-tree-iterator/
# Time complexity: hasNext() -- O(1), next() -- O(1) avg O(1)
# Space complexity: O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""

time O(1)
The average time complexity of next() function is O(1) indeed in your case. 
As the next function can be called n times at most, and the number of right 
nodes in self.pushAll(tmpNode.right) function is maximal n in a tree which 
has n nodes, so the amortized time complexity is O(1).

space O(1)
"""
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.get_left(root)

    def get_left(self, root):
        while root is not None:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        res = self.stack.pop()
        self.get_left(res.right)
        return res.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return True if self.stack else False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
