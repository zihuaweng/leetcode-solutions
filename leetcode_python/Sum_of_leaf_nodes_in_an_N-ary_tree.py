#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class Node:
    def __init__(self, val, children=[], right=None):
        self.val = val
        self.children = children
        self.right = right


def get_leaf_sum(head):
    if len(head.children) == 0:
        return head.val

    leaf_sum = 0
    while head:
        first = prev = None
        while head:
            for i in range(len(head.children)):
                if len(head.children[i].children) == 0:
                    leaf_sum += head.children[i].val

                if not first and len(head.children[i].children) > 0:
                    first = head.children[i]

                if prev:
                    prev.right = head.children[i]
                prev = head.children[i]
            head = head.right
            head = first

    return leaf_sum


# Test case:
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n2 = Node(2, [n4, n5])
n3 = Node(3, [n7])
n1 = Node(1, [n2, n3])
assert 16 == get_leaf_sum(n1)
