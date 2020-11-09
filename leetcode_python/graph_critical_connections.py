def find_critical_connections(graph):
    length = len(graph)
    rank = [-1] * length   # -1 表示没有visited
    ids = [-1] * length   # 表示走的顺序，第一次赋值是当前的rank里的level
    bridges = []
    
    def dfs(node, prev, level):
        rank[node] = ids[node] = level # rank赋值level记录了当前点的rank，而ids赋值level表示这个是第几个访问的点，这个id非常重要，因为需要用这个id判断是否走回了起点
  
        for child in graph[node]:
            if child == prev:
                continue
            if rank[child] == -1:
                dfs(child, node, level+1)
                rank[node] = min(rank[node], rank[child])
                if ids[node] < rank[child]:         # 如果返回的rank比我当前访问id要大，证明并没有回头路，是一个bridge
                    bridges.append([node, child])
            else:
                rank[node] = min(rank[node], ids[child])   # 如果已经走过了，比较子节点的level(就是访问时id)，和当前rank
    
    dfs(0, -1, 0)
    print(ids)
    return bridges


# 更加高效的写法
def find_critical_connections2(graph):
    length = len(graph)
    rank = [-1] * length   # -1 表示没有visited
    bridges = []
    
    def dfs(node, prev, level):
        rank[node] = level
  
        for child in graph[node]:
            if child == prev:         # 跳过父节点
                continue
            if rank[child] == -1:     # 只需要遍历没有visited过的
                dfs(child, node, level+1)
            
            # 上一步递归会把赋值更小的rank，如果子节点有更小的，意味有一个环，那么当前节点应该选择其中的最小值
            rank[node] = min(rank[node], rank[child])
            # 如果返回的rank比我当前访问id要大，证明并没有回头路，是一个bridge
            if rank[child] >= level+1:         
                bridges.append([node, child])
    
    dfs(0, -1, 0)
    return bridges
    
    
graph = {0:[1, 2],
        1:[0, 2],
        2:[0,1,3,5],
        3:[2, 4],
        4:[3],
        5:[2,6,8],
        6:[5,7],
        7:[6,8],
        8:[5,7]}


print(find_critical_connections(graph))