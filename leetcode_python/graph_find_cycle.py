# 当前路径放到on_stack， 如果我们走到下一个节点也在stack里面，证明有cycle
# 之前走完的节点要存到visited，下次不会继续访问
def find_cycle(graph):
    length = len(graph)
    visited = [False] * length # 保存子节点已经访问完的节点
    on_stack = [False] * length # 保存当前访问路径已经走过的节点
    
    def dfs(node):
        on_stack[node] = True    # 加当前节点到stack，意味着该节点是在当前路径中的
        for child in graph[node]:   
            if not visited[child]:   # 只看之前没有访问过的节点
                if on_stack[child]:  # 如果这个子节点是在当前访问的路径上，证明存在cycle
                    return True
                if dfs(child):       # 继续递归看下面的子节点
                    return True
        on_stack[node] = False    # 这里是回退，需要把访问的节点从stack中删除
        visited[node] = True     # 因为所有子节点都访问了，该节点可以改为finished
        return False
    
    for i in range(length):
        if not visited[i]:
            if dfs(i):
                return True
    return False
    
    
graph = {0:[1],
        1:[2],
        2:[0],
        3:[7, 4],
        4:[5],
        5:[0,6],
        6:[0,2,4],
        7:[3,5]}


print(find_cycle(graph))