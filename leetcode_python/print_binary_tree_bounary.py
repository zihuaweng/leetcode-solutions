"""
1.给一个 full binary tree，比如下面这个
				1
			2		3
    4	      5          6          7
8     9     10   11   12  13  14 15
让打印如下顺序 1,2,4,8,9,10,11,12,13,14,15,7,3,1

"""
class Node: 
    # Constructor to create a new node 
    def __init__(self, val): 
        self.val = val  
        self.left = None
        self.right = None


def print_leaves(root):
    if not root:
        return
    print_leaves(root.left)
    if not root.left and not root.right:  # 只要是叶子节点都打印
        print(root.val)
    print_leaves(root.right)


def print_left(root):
    if root.left:
        print(root.val)
        print_left(root.left)
    elif root.right:   # 左边境上可能只有右节点
        print(root.val)
        print_left(root.right)

    # 如果not root.left and not root.right 说明是叶子节点，留给print_leaves执行，否则会有重复

def print_right(root):
    if root.right:
        print_right(root.right)
        print(root.val)
    elif root.left:  # 右边境上可能只有左节点
        print_right(root.left)
        print(root.left)

    # 如果not root.left and not root.right 说明是叶子节点，留给print_leaves执行，否则会有重复


def print_boundary(root):
    if not root:
        return
    print(root.val)
    print_left(root.left)
    print_leaves(root)
    print_right(root.right)


root = Node(20) 
root.left = Node(8) 
root.left.left = Node(4) 
root.left.left.right = Node(5) 
root.left.left.right.right = Node(9) 
root.left.right = Node(12) 
root.left.right.left = Node(10) 
root.left.right.right = Node(14) 
root.right = Node(22) 
root.right.right = Node(25) 
print_boundary(root) 