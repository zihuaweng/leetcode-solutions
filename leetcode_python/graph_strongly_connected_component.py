
# 当前路径放到on_stack， 如果我们走到下一个节点也在stack里面，证明有cycle
def find_cycle(graph):
    length = len(graph)
    stack = [] # 保存当前访问的节点
    on_stack = [False] * length # 保存当前访问路径已经走过的节点
    rank = [-1] * length  # 记录当前的rank，如果有相同的rank，证明是同一个scc
    ids = [-1] * length   # 记录当前点是第几个访问的，用于判断是否有环，-1代表还没走过
    
    def dfs(node, visit_id):
        stack.append(node)
        on_stack[node] = True    # 加当前节点到stack，意味着该节点是在当前路径中的
        rank[node] = ids[node] = visit_id    # rank赋值visit_id记录了当前点的rank，而ids赋值visit_id表示这个是第几个访问的点，这个id非常重要，因为需要用这个id判断是否走回了起点

        for child in graph[node]: 
            if ids[child] == -1:   # 只看之前没有访问过的节点
                dfs(child, visit_id+1)       # 继续递归看下面的子节点

            if on_stack[child]:  # 如果这个子节点是在当前访问的路径上，证明存在scc，这一步需要在dfs后面，所以是一个回退的操作
                rank[node] = min(rank[node], rank[child])    # 取得最小的rank
            
        if ids[node] == rank[node]:
            while stack:
                n = stack.pop()
                rank[n] = ids[node]
                on_stack[n] = False
                if n == node:
                    break
        
    for i in range(length):
        if ids[i] == -1:
            dfs(i, i)
    return len(set(rank))
    
    
graph = {0:[1],
        1:[2],
        2:[0],
        3:[7,4],
        4:[5],
        5:[0,6],
        6:[0,2,4],
        7:[3,5]}


print(find_cycle(graph))