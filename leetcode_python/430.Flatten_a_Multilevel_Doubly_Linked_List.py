# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
# 用递归来做
# Time complexity: O(n)
# Space complexity: O(n)

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        p = head
        while p is not None:
            if p.child is not None:

                right = p.next

                p.next = self.flatten(p.child)
                p.next.prev = p
                p.child = None

                while p.next is not None:
                    p = p.next

                if right is not None:
                    p.next = right
                    p.next.prev = p

            p = p.next

        return head

