# 首先计算每个node能连接到多少个点：degree
# 从Leaf开始剪枝，Leaf是degree==1的node（或者==0，因为有孤岛），当前节点degree=0，连接节点degree-1
# 最后如果所有node都走过了，我们剩下的Leaf（会包含一个或者两个点）

def find_center(tree):
    n = len(tree)
    degree = [0] * n
    leaf = []
    for i in range(n):
        degree[i] = len(tree[i])
        if degree[i] <= 1:  # 保存初的Leaf，有可能是孤岛，degree==0
            leaf.append(i)
        
    count = len(leaf)
    while count < n:
        new_leaf = []    # bfs, 一层层遍历，下一层的node保存到一个新的list
        for i in leaf:
            for next_i in tree[i]:
                degree[next_i] -= 1
                if degree[next_i] == 1:   # 如果degree==1证明已经到了Leaf
                    new_leaf.append(next_i)
            degree[i] = 0
        count += len(new_leaf)
        leaf = new_leaf
    return leaf
            
tree = {
    0:[1],
    1:[0,3,4],
    2:[3],
    3:[1,2,6,7],
    4:[1,5,8],
    5:[4],
    6:[3,9],
    7:[3],
    8:[4],
    9:[6]
}

print(find_center(tree))