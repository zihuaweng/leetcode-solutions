"""
Given a root of a Binary Search Tree (BST) and a number num, implement an 
efficient function findLargestSmallerKey that finds the largest key in the 
tree that is smaller than num. If such a number doesn’t exist, return -1. 
Assume that all keys in the tree are nonnegative.
"""

def get_max_small_node(root, target):
    """
    1. traverse the tree
      if node.val > num: node -> node.left
      if node.val < num: node -> node.right
    2. if node.val < num: store node.val
    
    17
    20, l | 9, r | 12, r | 14, r
     
    12
    20,l | 9, r | 12, l| 11, r 
    
    9
    20, l | 9 l | 5 r
    
    13
    20, l | 9, r | 12 r | 14 l | 
    """
    prev = -1
    while root:
        if root.val < target:
            prev = root.val
            root = root.right
        else:
            root = root.left
    return prev
